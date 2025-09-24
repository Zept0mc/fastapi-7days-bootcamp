from fastapi import FastAPI, HTTPException
from models import Task, TaskResponse, taskUpdate

app = FastAPI()

tasks = []

@app.get("/")
def get_root():
    return{"Testing, attention please"}

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id >= len(tasks) or tasks[task_id].isDeleted:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = tasks[task_id]
    return TaskResponse(id=task_id, name=task.name, description=task.description, isDeleted=task.isDeleted)
    

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return TaskResponse(name=task.name, description=task.description, isDeleted=task.isDeleted, id=tasks.index(task))

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: taskUpdate):
    if task_id >= len(tasks) or tasks[task_id].isDeleted:
        raise HTTPException(status_code=404, detail="Task not found")

    stored_task = tasks[task_id]
    if task_update.name is not None:
        stored_task.name = task_update.name
    if task_update.description is not None:
        stored_task.description = task_update.description
    return TaskResponse(name=stored_task.name, description=stored_task.description, isDeleted=stored_task.isDeleted, id=task_id)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks[task_id].isDeleted = True
    return{"message":"Task deleted"}