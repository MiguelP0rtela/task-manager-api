from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    title: str
    content: str | None = None


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    content: str | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    content: str | None = None