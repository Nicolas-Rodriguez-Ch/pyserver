from fastapi import APIRouter
from abc import ABC, abstractmethod


class BaseRouter(ABC):
    prefix: str
    tags: list
    responses: dict

    def __init__(self):
        self.router = APIRouter(
            prefix=self.prefix,
            tags=self.tags,
            responses=self.responses
        )
        self.setup_routes()

    @abstractmethod
    def setup_routes(self):
        pass
