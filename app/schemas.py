from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime, date

from .models import TaskPriority, UserBase, TaskBase

# User
class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id:int

# Tasks
class TaskCreate(TaskBase):
    pass

class TaskUpdate(SQLModel):
    title:str | None = None
    description:str | None = None
    completed: bool | None = None
    priority:TaskPriority | None = None
    due_date:date | None = None
    owner_id:int | None = None
class TaskRead(TaskBase):
    id:int
    
class TaskReadWithOwner(TaskRead):
    owner: Optional[UserRead] = None