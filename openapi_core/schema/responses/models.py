"""OpenAPI core responses models module"""
from openapi_core.schema.media_types.exceptions import InvalidContentType
from openapi_core.schema.responses.exceptions import MissingResponseContent


class Response(object):

    def __init__(
            self, http_status, description, headers=None, content=None,
            links=None):
        self.http_status = http_status
        self.description = description
        self.headers = headers and dict(headers) or {}
        self.content = content and dict(content) or {}
        self.links = links and dict(links) or {}

    def __getitem__(self, mimetype):
        try:
            return self.content[mimetype]
        except KeyError:
            raise InvalidContentType(
                "Invalid mime type `{0}`".format(mimetype))

    def get_value(self, response):
        if not response.data:
            raise MissingResponseContent("Missing response content")

        return response.data
