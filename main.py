from fastapi import FastAPI
from routers import tasks

app = FastAPI(
    title='To-Do API',
    description='API для управления задачами',
    version='1.0.0'
)

app.include_router(tasks.router)

@app.get('/')
def root():
    return {'message': 'Добро пожаловать в API! Перейдите на /docs для документации.'}