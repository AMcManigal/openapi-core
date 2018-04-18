"""OpenAPI core media types models module"""
from openapi_core.schema.media_types.exceptions import InvalidMediaTypeValue
from openapi_core.schema.schemas.exceptions import InvalidSchemaValue


class MediaType(object):
    """Represents an OpenAPI MediaType."""

    def __init__(self, mimetype, schema=None):
        self.mimetype = mimetype
        self.schema = schema

    def unmarshal(self, value):
        if not self.schema:
            return value

        try:
            return self.schema.unmarshal(value)
        except InvalidSchemaValue as exc:
            raise InvalidMediaTypeValue(str(exc))
