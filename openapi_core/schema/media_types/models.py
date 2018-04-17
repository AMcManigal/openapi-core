"""OpenAPI core media types models module"""
from openapi_core.exceptions import InvalidValueType, InvalidMediaTypeValue


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
        except InvalidValueType as exc:
            raise InvalidMediaTypeValue(str(exc))
