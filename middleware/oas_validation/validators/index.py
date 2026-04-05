from openapi_core import OpenAPI


_openapi: OpenAPI | None = None


def get_validator(app) -> OpenAPI:
    global _openapi
    if _openapi is None:
        _openapi = OpenAPI.from_dict(app.openapi())
    return _openapi
