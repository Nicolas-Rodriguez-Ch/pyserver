from repositories import GameRepository
from sqlalchemy.ext.asyncio import AsyncSession


class GameService:
    def __init__(self, repository: GameRepository):
        self.repository = repository

    async def get_all_games(self, session: AsyncSession):
        try:
            return await self.repository.get_all(session)
        except:
            raise

    async def create_game(self, session: AsyncSession, game_data: dict):
        try:
            game = await self.repository.create(session, game_data)
            return game
        except:
            raise
