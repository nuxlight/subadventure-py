from typing import Any
from fastapi import APIRouter
from app.crud import user
from app.db.database import SessionLocal
from app.schemas.user import UserBase, UserCreate

router = APIRouter(prefix="/user")


@router.put("/sample", response_model=UserBase)
async def getSample(
    user_in: UserCreate
) -> Any:
    return user_in
