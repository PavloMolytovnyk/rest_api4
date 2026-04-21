from fastapi import APIRouter, Depends, Query
from motor.motor_asyncio import AsyncIOMotorDatabase
from database import get_db
from schemas.book import BookCreate, BookResponse
from repository import book_repository
from typing import List

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=List[BookResponse])
async def get_books(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: AsyncIOMotorDatabase = Depends(get_db)
):
    return await book_repository.get_all(db, limit, offset)

@router.post("/", response_model=BookResponse, status_code=201)
async def create_book(book: BookCreate, db: AsyncIOMotorDatabase = Depends(get_db)):
    return await book_repository.add(db, book.model_dump())