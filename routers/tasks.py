from fastapi import APIRouter, HTTPException
from typing import Optional

from models import Task

router = APIRouter(
    prefix='/tasks',
    tags=['Задачи']
)

fake_db_tasks = []

@router.get('')
def get_tasks():
    return fake_db_tasks

"""
Path parameter
"""
@router.get('/task/{id}')
async def detail_task(id: int) -> dict:
    for task in fake_db_tasks:
        if task['id'] == id:
            return task

    raise HTTPException(status_code=404, detail='Page Not Found')

"""
Query parameter
"""
@router.get('/search')
async def search(task_id: Optional[int] = None)-> dict:
    if task_id:
        for task in fake_db_tasks:
            if task['id'] == task_id:
                return task

        raise HTTPException(status_code=404, detail='Page Not Found')

    else:
        raise HTTPException(status_code=404, detail='че ты передал в поисковую строку чтобы ошибка вышла?')


@router.post('/tasks')
async def create_task(task: Task):
    new_task = task.dict()
    new_task['id'] = len(fake_db_tasks) + 1

    fake_db_tasks.append(new_task)
    return {
        'message': 'ты гений',
        'task': task
    }

@router.put('/tasks/{task_id}')
async def update_task(task_id: int, task: Task):
    for idx, existing_task  in enumerate(fake_db_tasks):
        if existing_task ['id'] == task_id:
            updated_task = task.model_dump()
            updated_task["id"] = task_id
            fake_db_tasks[idx] = updated_task

            return {
                'message': 'ты гений',
                'task': task
            }

    raise HTTPException(status_code=404, detail='Mission Not Found')

@router.delete('/tasks/{task_id}')
async def del_task(task_id: int):
    for idx, existing_task in enumerate(fake_db_tasks):
        if existing_task['id'] == task_id:
            del fake_db_tasks[idx]

            return {'message': 'ты гений'}

    raise HTTPException(status_code=404, detail='Mission Not Found')