from dataclasses_avroschema.pydantic import AvroBaseModel
from pydantic import Field, EmailStr
from datetime import datetime


class OTPAvroIn(AvroBaseModel):
     purpose: str = Field(description='The purpose of sending the one-time-password')
     firstname: str = Field(description="A string. This is the user's first name.",
                           examples=['John'])
     email: EmailStr = Field(description='Email associated with the account')
     phone_number: str = Field(description='Phone number associated with the account')
     

class OTPAvroOut(OTPAvroIn):
     otp: str = Field(description="One-time-password")
     created_on: datetime = Field(description='This is the date the otp was created', default=datetime.utcnow())
     expires_on: datetime = Field(description='Expiration time of the otp')

