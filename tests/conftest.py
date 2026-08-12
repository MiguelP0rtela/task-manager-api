import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.core.config import settings
from app.database.database import Base, get_db
from app.main import app
from app.models.user import User
from app.core.security import hash_password

engine = create_engine(settings.test_database_url)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def admin_user():
    db = TestingSessionLocal()

    user = User(
        username="admin",
        email="admin@gmail.com",
        password=hash_password("Admin123!"),
        role="admin",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    db.close()

    return user
