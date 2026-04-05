from fastapi import Request, Response
from fastapi import HTTPException
from ..base import BaseMiddleware
from openapi_core.protocols import Request as OpenAPIRequest
from openapi_core.protocols import Response as OpenAPIResponse


class OasValidation(BaseMiddleware):
    def __init__(self, oas_validator):
        self.oas_validator = oas_validator

    async def process_request(self, request: Request):
        print(f"Validating request: {request.method} {request.url.path}")
        body = await request.body()
        method = request.method
        full_url = str(request.url)
        mimetype = request.headers.get("content-type", "application/json")

        async def receive():
            return {
                "type": "http.request",
                "body": body
            }

        openapi_request = OpenAPIRequest(full_url_uri=full_url, method=method.lower(), body=body, mimetype=mimetype,
                                         parameters={"header": dict(request.headers)})
        request._receive = receive
        try:
            self.oas_validator.validate(openapi_request)
        except Exception as e:
            print(f"Request validation failed: {str(e)}")
            raise HTTPException(status_code=422, detail=str(e))

    async def process_response(self, response: Response):
        print(f"Validating response: {response.status_code} {response.body}")
        body = response.body
        openapi_response = OpenAPIResponse(status_code=response.status_code, headers=response.headers,
                                           content_type=response.content_type, data=body)
        try:
            self.oas_validator.validate(openapi_response)
        except Exception as e:
            print(f"Response validation failed: {str(e)}")