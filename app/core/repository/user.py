from sqlalchemy.orm import Session
from core.hashing import Hash
from core import schemas, models

def register_user(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name, 
        email=request.email, 
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(email: str, db: Session):
    user = db.query(models.User).filter(models.User.email == email).first()
    return user