from datetime import date

from sqlmodel import SQLModel

from .models import TaskBase, TaskPriority, UserBase


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class TaskCreate(TaskBase):
    pass


class TaskUpdate(SQLModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None
    priority: TaskPriority | None = None
    due_date: date | None = None
    owner_id: int | None = None


class TaskRead(TaskBase):
    id: int


class TaskReadWithOwner(TaskRead):
    owner: UserRead | None = None