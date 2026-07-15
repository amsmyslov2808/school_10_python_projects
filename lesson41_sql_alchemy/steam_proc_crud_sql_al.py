from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/steam_db"


class Base(DeclarativeBase):
    pass
