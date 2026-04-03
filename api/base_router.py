from fastapi import APIRouter, Depends
from db import db_manager
from abc import ABC, abstractmethod


class BaseRouter(ABC):
    prefix: str
    tags: list
    responses: dict

    def __init__(self):
        self.router = APIRouter(
            prefix=self.prefix, tags=self.tags, responses=self.responses
        )
        self.session_dependency = self.get_session_dependency()
        self.setup_routes()

    @abstractmethod
    def setup_routes(self):
        pass

    def get_session_dependency(self):
        return Depends(db_manager)
