from fastapi import HTTPException
from models import Game
from repositories import GameRepository
from schemas import GameCreate, GameResponse
from services import GameService
from ..base_router import BaseRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class GamesRouter(BaseRouter):
    prefix = "/games"
    tags = ["Games"]
    responses = {404: {"description": "service not found"}}

    def setup_routes(self):
        @self.router.get("/")
        async def get_all_games(session: AsyncSession = self.session_dependency):
            try:
                repository = GameRepository()
                service = GameService(repository)

                games = await service.get_all_games(session)
                games_response = [GameResponse.model_validate(game) for game in games]
                return {"description": "Games found!", "games": games_response}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.post("/")
        async def create_game(
            game: GameCreate, session: AsyncSession = self.session_dependency
        ):
            try:
                repository = GameRepository()
                service = GameService(repository)

                game_dict = game.model_dump()
                new_game = await service.create_game(session, game_dict)
                new_game_response = GameResponse.model_validate(new_game)
                return {
                    "description": "New game cretaed successfuly",
                    "new_game": new_game_response,
                }
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))


router = GamesRouter().router
