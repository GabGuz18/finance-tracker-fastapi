import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone

from app.db.deps import get_db
from app.models.user import User
from app.repositories.users import get_user_by_email, create_user
from app.schemas.auth import RegisterIn, LoginIn, TokenOut
from app.core.security import hash_password, verify_password, create_access_token, create_refresh_token


router = APIRouter(prefix="/auth")

@router.post("/register", response_model=TokenOut, status_code=status.HTTP_201_CREATED)
async def register(data: RegisterIn, db: AsyncSession = Depends(get_db)):
    existing = await get_user_by_email(db, data.email)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    user = User(
        id_user=uuid.uuid4(),
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        hashed_password=hash_password(data.password),
        registered_at = datetime.now(timezone.utc)
    )
    user = await create_user(db, user)

    return TokenOut(
        access_token=create_access_token(str(user.id_user)),
        refresh_token=create_refresh_token(str(user.id_user)),
    )

@router.post("/login", response_model=TokenOut)
async def login(data: LoginIn, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_email(db, data.email)
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")

    return TokenOut(
        access_token=create_access_token(str(user.id_user)),
        refresh_token=create_refresh_token(str(user.id_user)),
    )
