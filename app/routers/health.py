from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Task Manager API"}


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.get("/version")
def health():
    return {"version": "1.0.0"}
