from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    name: str
    description: str
    isDeleted: bool = False


class TaskResponse(Task):
    id: int

class taskUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None