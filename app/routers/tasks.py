from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from sqlalchemy.orm import Session

from app.database import  SessionLocal
from app.models.task import Task as TaskModel
from app.schemas.schemas import Task as TaskSchema

router = APIRouter(
    prefix='/tasks',
    tags=['Задачи']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/')
def get_tasks(db: Session = Depends(get_db)):
    return db.query(TaskModel).all()


@router.get('/{task_id}')
def detail_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail='Not Found')
    return task


@router.post('/')
def create_task(task: TaskSchema, db: Session = Depends(get_db)):
    new_task = TaskModel(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.put('/{task_id}')
def update_task(task_id: int, task: TaskSchema, db: Session = Depends(get_db)):
    existing = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail='Not Found')

    for key, value in task.model_dump().items():
        setattr(existing, key, value)

    db.commit()
    db.refresh(existing)
    return existing


@router.delete('/{task_id}')
def del_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail='Not Found')

    db.delete(task)
    db.commit()
    return {'message': 'ты гений'}
