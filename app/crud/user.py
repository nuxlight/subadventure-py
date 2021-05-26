from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.db.models import User


def create_user(db: Session, user: UserCreate, password: str):
    db_user = User(name=user.name, password=password, token="")
    return user
