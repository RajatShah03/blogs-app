from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from core.database import get_db
from core.repository import blog
from core.oauth2 import get_current_user
from core import schemas

router = APIRouter(
    prefix='/blog',
    tags=['Blogs'],
)

@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create_blog(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.delete_blog(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def modify(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update_blog(id, request, db)

@router.get('', status_code=200, response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all_blogs(db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_blog(id, response, db)
