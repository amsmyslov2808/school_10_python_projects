"""Настройка подключения к базе данных PostgreSQL."""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Доступы к учебной базе данных хранятся прямо в коде по условию задания.
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "12345"
DATABASE_HOST = "localhost"
DATABASE_PORT = 5432
DATABASE_NAME = "travel_hunter_db"

# В строке подключения указан драйвер psycopg для работы SQLAlchemy с PostgreSQL.
DATABASE_URL = (
    f"postgresql+psycopg://{DATABASE_USER}:{DATABASE_PASSWORD}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)


class Base(DeclarativeBase):
    """Общий базовый класс всех таблиц SQLAlchemy."""


# pool_pre_ping проверяет соединение перед выдачей из пула и помогает пережить
# разрыв простаивавшего подключения к PostgreSQL.
engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)

# Фабрика создаёт отдельную сессию для каждой операции репозитория.
get_session = sessionmaker(
    bind=engine,
    expire_on_commit=True,
)
