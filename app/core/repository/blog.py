from fastapi import HTTPException, Response, status
from sqlalchemy import delete, update
from sqlalchemy.orm import Session
from core import schemas, models

def create_blog(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    # db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    # db.commit()
    stmt = delete(models.Blog).where(models.Blog.id == id).execution_options(synchronize_session="fetch")
    db.execute(stmt)
    db.commit()
    return {'detail': 'blog deleted'}

def update_blog(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    # db.query(models.Blog).filter(models.Blog.id == id).update(request, synchronize_session=False)
    # db.commit()
    stmt = update(models.Blog).where(models.Blog.id == id).values(title=request.title, body=request.body).execution_options(synchronize_session="fetch")
    db.execute(stmt)
    db.commit()
    return {'detail': 'blog updated'}

def get_all_blogs(db: Session):
    all_blogs = db.query(models.Blog).all()
    return all_blogs

def get_blog(id: int, response: Response, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Blog with id {id} is not found'
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return { 'detail': f'Blog with id {id} is not found' }
    return blog