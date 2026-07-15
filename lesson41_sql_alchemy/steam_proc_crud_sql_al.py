from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped
)

DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/steam_db"


class Base(DeclarativeBase):
    pass


class UserRole(Base):
    __tablename__ = "user_roles"
    
    id: Mapped[int] = 
    role_name: Mapped[str] = 
    description: Mapped[str] =
    
