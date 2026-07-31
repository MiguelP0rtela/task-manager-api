from fastapi import FastAPI

from app.routers.health import router as health_router
from app.routers.users import router as users_router
from app.routers.auth import router as users_auth
from app.routers.tasks import router as users_tasks

app = FastAPI()

app.include_router(health_router)
app.include_router(users_router)
app.include_router(users_auth)
app.include_router(users_tasks)
