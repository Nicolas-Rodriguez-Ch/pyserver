from fastapi import FastAPI
from openapi_core.contrib.fastapi.middlewares import FastAPIOpenAPIMiddleware
from .oas_validation import get_validator


class MiddlewareManager:
    def __init__(self, app: FastAPI):
        self.app = app

    def register_middlewares(self):
        validator = get_validator(self.app)

        self.app.add_middleware(FastAPIOpenAPIMiddleware, openapi=validator)
