from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.db import models


def create_user(db: Session, user: UserCreate) -> models.User:
    db_user = models.User(
        name=user.name, password=user.password, token=user.token)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
