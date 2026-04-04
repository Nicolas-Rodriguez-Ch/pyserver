from fastapi import HTTPException
from repositories import GameRepository
from schemas.games import GameResponse
from services import GameService
from ..base_router import BaseRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class GamesRouter(BaseRouter):
    prefix = "/games"
    tags = ["Games"]
    responses = {404: {"message": {"service not found"}}}

    def setup_routes(self):
        @self.router.get("/")
        async def get_all_games(session: AsyncSession = self.session_dependency):
            try:
                repository = GameRepository()
                service = GameService(repository)

                games = await service.get_all_games(session)
                games_response = [GameResponse.model_validate(game) for game in games]
                return {"message": "Games found!", "games": games_response}
            except Exception as e:
                raise HTTPException(status_code=500, detail=e)


router = GamesRouter().router
