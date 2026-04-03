from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from models import Game
from sqlalchemy import select


class GameRepository:
    def __init__(self):
        pass

    async def get_all(self, session: AsyncSession) -> List[Game]:
        try:
            statement = select(Game)
            result = await session.execute(statement)
            games = list(result.scalars().all())
            return games
        except Exception:
            raise

    async def create(self, session: AsyncSession, game_data: dict) -> Game:
        try:
            new_game = Game(**game_data)
            session.add(new_game)
            await session.commit()
            await session.refresh(new_game)
            return new_game
        except Exception:
            await session.rollback()
            raise
