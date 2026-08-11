from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from app.core.security import verify_password, create_access_token, create_refresh_token
from app.database.database import get_db
from app.models.user import User
from fastapi.security import OAuth2PasswordRequestForm
from app.models.refresh_token import RefreshToken
from app.schemas.token import RefreshTokenRequest

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    if not verify_password(
            form_data.password,
            user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    access_token = create_access_token(
        {"sub": user.email}
    )

    refresh_token = create_refresh_token()

    db.query(RefreshToken).filter(
        RefreshToken.user_id == user.id,
        RefreshToken.revoked == False
    ).update(
        {"revoked": True}
    )

    refresh_token_db = RefreshToken(
        token=refresh_token,
        expires_at=datetime.now(timezone.utc) + timedelta(days=30),
        user_id=user.id
    )

    db.add(refresh_token_db)
    db.commit()
    db.refresh(refresh_token_db)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


@router.post("/refresh")
def refresh_access_token(
        request: RefreshTokenRequest,
        db: Session = Depends(get_db)
):
    refresh_token_db = db.query(
        RefreshToken
    ).filter(
        RefreshToken.token == request.refresh_token
    ).first()

    if refresh_token_db is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token."
        )

    if refresh_token_db.revoked:
        raise HTTPException(
            status_code=401,
            detail="Refresh token revoked."
        )

    if refresh_token_db.expires_at < datetime.now(timezone.utc):
        raise HTTPException(
            status_code=401,
            detail="Refresh token expired."
        )

    user = db.query(User).filter(
        User.id == refresh_token_db.user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    access_token = create_access_token(
        {
            "sub": user.email
        }
    )

    refresh_token_db.revoked = True

    new_refresh_token = create_refresh_token()

    new_refresh_token_db = RefreshToken(
        token=new_refresh_token,
        expires_at=datetime.now(timezone.utc) + timedelta(days=30),
        user_id=user.id
    )

    db.add(new_refresh_token_db)
    db.commit()
    db.refresh(new_refresh_token_db)

    return {
        "access_token": access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer"
    }


@router.post("/logout")
def logout(
        request: RefreshTokenRequest,
        db: Session = Depends(get_db)
):
    refresh_token_db = db.query(
        RefreshToken
    ).filter(
        RefreshToken.token == request.refresh_token
    ).first()

    if refresh_token_db is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token."
        )

    if refresh_token_db.revoked:
        raise HTTPException(
            status_code=401,
            detail="Refresh token already revoked."
        )

    refresh_token_db.revoked = True

    db.commit()

    return {
        "message": "Logged out successfully."
    }
