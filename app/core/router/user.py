from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.database import get_db
from core.repository import user
from core import schemas

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def register(request: schemas.User, db: Session = Depends(get_db)):
    return user.register_user(request, db)

@router.get('/{email}', status_code=200, response_model=schemas.ShowUser)
def show_user(email: str, db: Session = Depends(get_db)):
    return user.get_user(email, db)