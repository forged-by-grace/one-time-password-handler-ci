from dataclasses_avroschema.pydantic import AvroBaseModel
from pydantic import Field
from datetime import datetime


class ServiceError(AvroBaseModel):
    service_name: str = Field(description="Name of the service generating the error")
    error: str = Field(description="Error that occured")
    occurred_at: datetime = Field(description="Timestamp of error", default=datetime.utcnow())