from fastapi import APIRouter, Depends, HTTPException, Response
from pip._internal.cli import status_codes
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate

from app.core.security import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(
        task: TaskCreate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    new_task = Task(
        title=task.title,
        content=task.content,
        user_id=current_user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.get("/", response_model=list[TaskResponse])
def get_tasks(
        current_user: User = Depends(get_current_user),
):
    return current_user.tasks


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
        task_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    return task


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
        task_id: int,
        task_update: TaskUpdate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    if task_update.title is not None:
        task.title = task_update.title

    if task_update.content is not None:
        task.content = task_update.content

    db.commit()
    db.refresh(task)

    return task


@router.delete("/{task_id}", status_code=204)
def delete_task(
        task_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    db.delete(task)
    db.commit()

    return Response(status_code=204)
