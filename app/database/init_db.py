from app.database.database import Base, engine
from app.models.user import User
from app.models.task import Task

Base.metadata.create_all(bind=engine)

print("Base de dados inicializada com sucesso!")
