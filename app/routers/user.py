from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import user
from app.db.database import SessionLocal, engine
from app.schemas.user import UserBase, UserCreate

user.models.Base.metadata.create_all(engine)

router = APIRouter(prefix="/user")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.put("/")
async def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db)
) -> Any:
    return user.create_user(db, user_in)
