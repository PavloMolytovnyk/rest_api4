from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class BookStatus(str, Enum):
    available = "available"
    borrowed = "borrowed"

class BookCreate(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    description: Optional[str] = None
    status: BookStatus = BookStatus.available
    year: int = Field(..., gt=0)

class BookResponse(BookCreate):
    id: str = Field(..., alias="_id")

    class Config:
        populate_by_name = True