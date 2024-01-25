from dataclasses_avroschema.pydantic import AvroBaseModel
from pydantic import Field
from core.enums.enum import *
from typing import Dict


class Cache(AvroBaseModel):
    key: str = Field(description='Key to retrieve the cache')
    data: bytes = Field(description='Data to be cached')