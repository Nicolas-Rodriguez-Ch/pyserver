from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from db import Base


class Game(Base):
    __tablename__ = "games"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    map = Column(String(50), nullable=False)
    role = Column(String(20), nullable=False)
    mode = Column(String(20), nullable=False)
    outcome = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )
