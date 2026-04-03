from ..base_router import BaseRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class GamesRouter(BaseRouter):
    prefix = "/games"
    tags = ["Games"]
    responses = {404: {"message": {"service nort found"}}}

    def setup_routes(self):
        @self.router.get("/")
        async def get_all_games(session: AsyncSession = self.session_dependency):
            return {"message": "Endpoint is available"}


router = GamesRouter().router
