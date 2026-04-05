from fastapi import FastAPI

from .oas_validation import OasValidation, get_validator


class MiddlewareManager:
    def __init__(self, app: FastAPI):
        self.app = app

    def register_middlewares(self):
        validator = get_validator(self.app)
        oas_validation = OasValidation(validator)

        @self.app.middleware("http")
        async def oas_validation_middleware(request, call_next):
            return await oas_validation.middleware(request, call_next)
