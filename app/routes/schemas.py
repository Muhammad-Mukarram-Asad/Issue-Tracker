from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class IssueStatus(str, Enum):
    open = "open",
    in_progress = "in progress",
    closed = "closed"

class IssuePriority(str, Enum):
    low = "low",
    medium = "medium",
    high = "high"

class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=50, examples=["Login button unresponsive"])
    description: str = Field(min_length=10, max_length=1000, examples=["Clicking login does nothing on Safari"])
    priority: IssuePriority = IssuePriority.low

class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=50, examples=["Login button unresponsive"])
    description: Optional[str] = Field(default=None, max_length=1000, examples=["Clicking login does nothing on Safari"])
    priority: Optional[IssuePriority] = None
    status: Optional[IssueStatus] = None

class IssueOut(BaseModel):
    id: str
    title: str
    description: str
    priority: IssuePriority
    status: IssueStatus