from enum import Enum

class NotificationChannel(str, Enum):
     email= "email"
     sms="sms"
     push_notification = "push_notification"


class NotificationTemplate(str, Enum):
     email_verification = "email_verification"
     phone_verification='Phone_verification'
     forgot_password='Forgot_password'
     reset_password='Reset_password'
     new_account_registration='new_account_registration'
     transaction_verification='Transaction_verification'
     

class OTP_Purpose(str, Enum):
     email_verification='email_verification'
     phone_verification='phone_verification'
     forgot_password='forgot_password'
     reset_password='reset_password'
     transaction_verification='transaction_verification'
     
