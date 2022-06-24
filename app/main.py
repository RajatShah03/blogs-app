from fastapi import FastAPI
from core import models
from core.database import engine
from core.router import blog, user, authentication

app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

models.Base.metadata.create_all(engine)

