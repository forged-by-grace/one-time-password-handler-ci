from core.model.notification_avro_model import Notification
from core.model.otp_avro_model import OTPAvroOut, OTPAvroIn
from datetime import datetime, timedelta
import secrets
import string
from core.utils.settings import settings
from core.event.produce_event import produce_event
from core.model.cache_model import Cache
from core.utils.init_log import logger
from core.helper.encryption_helper import encrypt
from core.enums.enum import NotificationChannel, NotificationTemplate

async def generate_otp(length: int):
    alphabet = string.ascii_letters + string.digits
    while True:
        otp = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in otp)
                and any(c.isupper() for c in otp)
                and sum(c.isdigit() for c in otp) >= 3):
            break    
    return otp


async def process_otp(data: OTPAvroIn) -> None:
    # Generate otp
    logger.info('Generating otp.')
    otp = await generate_otp(length=6)

    # Set expiry time
    otp_expiry = datetime.utcnow() + timedelta(hours=settings.otp_expiry_in_hours)

    # Convert otp model to dict
    otp_dict = data.model_dump()            

    # Encrypt otp
    encrypted_otp = encrypt(value=otp)

    # Update otp dict
    otp_dict.update({'otp': encrypted_otp, 'created_on': datetime.utcnow(), 'expires_on': otp_expiry})


    # Create avro obj
    otp_avro_obj = OTPAvroOut(**otp_dict)
    
    # Create notification obj
    notification = Notification(
        recipient_name=data.firstname,
        send_to=data.email,
        channel=NotificationChannel.email,
        content={"otp": otp, "expiry_hours": settings.otp_expiry_in_hours},
        template=NotificationTemplate.email_verification
    )

    # Serialize 
    otp_cache_event = otp_avro_obj.serialize()

    # Create a cache obj
    key=f"otp:{otp_avro_obj.email}-{otp_avro_obj.otp}-{otp_avro_obj.purpose.lower()}"
    print(f"OTP key: {key}")
    cache_obj = Cache(
        key=key,
        data=otp_cache_event
    )

    # Serialize
    cache_event = cache_obj.serialize()
    notification_event = notification.serialize()
    
    # Emit event
    logger.info('Emitting cache event.')
    logger.info('Emitting notification event.')
    await produce_event(topic=settings.api_cache_topic, value=cache_event)
    await produce_event(topic=settings.api_notification_topic, value=notification_event)              
