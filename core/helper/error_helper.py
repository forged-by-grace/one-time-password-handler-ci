from core.model.error_model import ServiceError
from core.utils.settings import settings
from core.event.produce_event import produce_event


async def log_error(error: str):
    # Create error obj
    error_obj = ServiceError(service_name=settings.service_name, error=error)

    # Serialize obj
    error_serialized = error_obj.serialize()

    # Produce error event
    await produce_event(topic=settings.api_error_topic, value=error_serialized)

