from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr, HttpUrl
import os

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.abspath('.env'), env_file_encoding='utf-8')
    # Event Streaming Server
    api_event_streaming_host: str
    api_event_streaming_client_id: str

    # OTP meta
    otp_expiry_in_hours: int

    # Streaming topics
    api_otp_topic: str
    api_cache_topic: str
    api_notification_topic: str
    api_error_topic: str

    # Streaming consumer group
    api_otp_group: str

    # Service metadata
    service_name: str

settings = Settings()
