from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Доступы к учебной базе данных. Они заданы прямо в коде по условию задания.
DATABASE_USER = "itpark-travel-hunter-bot-user"
DATABASE_PASSWORD = "JkyB1hPGd4UGEOUbNKPXZVKFiaIf3mjl1Qv9ucjufus="
DATABASE_HOST = "itpark-travel-hunter-bot-prod.postgres.svc.cluster.local"
DATABASE_PORT = 5432
DATABASE_NAME = "itpark-travel-hunter-bot"

DATABASE_URL = (
    f"postgresql+psycopg://{DATABASE_USER}:{DATABASE_PASSWORD}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)


class Base(DeclarativeBase):
    """Общий базовый класс всех таблиц SQLAlchemy."""


# pool_pre_ping проверяет соединение перед запросом и помогает после обрывов сети.
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)


def create_tables():
    """Создаёт таблицы, если они ещё отсутствуют в базе данных."""

    # Импорт нужен, чтобы SQLAlchemy узнал о модели VisitedCity перед созданием.
    from models.visited_city import VisitedCity

    Base.metadata.create_all(engine)
