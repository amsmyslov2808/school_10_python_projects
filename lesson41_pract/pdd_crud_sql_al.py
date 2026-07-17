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

DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/pdd_db"


class Base(DeclarativeBase):
    pass


class SignCategory(Base):
    __tablename__ = "sign_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)


class RoadSign(Base):
    __tablename__ = "road_signs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False)

    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("sign_categories.id", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=False,
    )

    category: Mapped[SignCategory] = relationship(back_populates="sign_categories")

    image_path: Mapped[str] = mapped_column(String(2000), nullable=False)


engine = create_engine(DATABASE_URL, echo=False)

get_session_local = sessionmaker(
    bind=engine,
    expire_on_commit=True,
)

with get_session_local() as session:
    print("ok")
