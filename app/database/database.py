from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = (
    "postgresql://taskmanager:password@localhost:5432/task_manager"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


class Base(DeclarativeBase):
    pass


from typing import Generator


def get_db() -> Generator:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
