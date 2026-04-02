from fastapi import APIRouter
from ..base_router import BaseRouter


class GamesRouter(BaseRouter):
    prefix = "/games"
    tags = ["Games"]
    responses = {404: {"message": {"service nort found"}}}

    def setup_routes(self):
        @self.router.get("/")
        async def games():
            return {"message": "Endpoint is available"}


router = GamesRouter().router
