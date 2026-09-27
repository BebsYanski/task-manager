from sqlmodel import SQLModel
import datetime
from sqlmodel.main import Field, Relationship
from enum import Enum
from typing import Optional

def utc_now()-> datetime.datetime:
    return datetime.datetime.now(datetime.UTC)

class TaskPriority(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class UserBase(SQLModel):
    name:str = Field(index = True)
    email: str = Field(unique = True, index = True)
    address:str = Field(index = True)
    
    tasks: list["Task"] = Relationship(back_populates="owner")

class User(UserBase,table = True):
    id:int | None = Field(default = None,primary_key = True)

class TaskBase(SQLModel):
    title:str = Field(index = True)
    description:str | None
    completed: bool = Field(default = False)
    priority:TaskPriority = Field(default = TaskPriority.MEDIUM, index = True)
    due_date:datetime.date | None = None
    created_at = datetime.datetime = Field(default_factory=utc_now)
    completed_at = Optional[datetime.datetime] = None
    
    owner_id:int | None = Field(default = None, foreign_key="user_id")
    owner: User | None = Relationship(back_populates="tasks")

class Task(TaskBase,table=True):
    id:Optional[int] = Field(default=None, primary_key=True)