from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    create_engine,
    select,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    joinedload,
    mapped_column,
    relationship,
    sessionmaker,
)

DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/steam_db"


class Base(DeclarativeBase):
    pass


class UserRole(Base):
    __tablename__ = "user_roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    role_name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
