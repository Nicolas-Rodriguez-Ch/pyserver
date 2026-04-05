from fastapi import Request, Response
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)


class BaseMiddleware(ABC):

    async def middleware(self, request, call_next):
        await self.process_request(request)
        response = await call_next(request)
        await self.process_response(response)
        return response

    @abstractmethod
    async def process_request(self, request: Request):
        pass

    @abstractmethod
    async def process_response(self, response: Response):
        pass
