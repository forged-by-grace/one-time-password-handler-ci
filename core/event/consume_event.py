from core.helper.consumer_helper import consume_event
from core.model.otp_avro_model import OTPAvroIn
from core.utils.settings import settings
from core.helper.otp_helper import process_otp
from core.utils.init_log import logger


async def create_otp_event():
    # consume event
    consumer = await consume_event(topic=settings.api_otp_topic, group_id=settings.api_otp_group)
    
    try:
        # Consume messages
        async for msg in consumer:
            logger.info('Received new otp event.')
            # Deserialize event
            otp_data = OTPAvroIn.deserialize(data=msg.value)
            
            # Process otp
            logger.info('Processing OTP...')
            await process_otp(data=otp_data)
    except Exception as err:
        logger.error(f"Failed to process event due to error: {str(err)}")
    finally:
        await consumer.stop()

    