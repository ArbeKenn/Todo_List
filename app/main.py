from fastapi import FastAPI
from app.routers import tasks
from app.models import task
from app.database import engine
from app.models.task import Base

app = FastAPI(
    title='To-Do API',
    description='API для управления задачами',
    version='1.0.0'
)
Base.metadata.create_all(bind=engine)

app.include_router(tasks.router)

@app.get('/')
def root():
    return {
        'message': 'Добро пожаловать в API! Перейдите на /docs для документации.'
    }