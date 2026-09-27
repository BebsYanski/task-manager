import datetime
from enum import Enum
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


def utc_now() -> datetime.datetime:
    return datetime.datetime.now(datetime.UTC)


class TaskPriority(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class UserBase(SQLModel):
    name: str = Field(index=True, min_length=1, max_length=50)
    email: str = Field(unique=True, index=True)
    age: int | None = Field(default=None, ge=1, le=150)
    address: str = Field(index=True)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tasks: list["Task"] = Relationship(back_populates="owner")


class TaskBase(SQLModel):
    title: str = Field(index=True)
    description: str | None = None
    completed: bool = Field(default=False)
    priority: TaskPriority = Field(default=TaskPriority.MEDIUM, index=True)
    due_date: datetime.date | None = None
    created_at: datetime.datetime = Field(default_factory=utc_now)
    completed_at: datetime.datetime | None = None


class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner_id: int | None = Field(default=None, foreign_key="user.id")
    owner: "User" | None = Relationship(back_populates="tasks")