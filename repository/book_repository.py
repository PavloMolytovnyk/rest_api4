from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId

async def get_all(db: AsyncIOMotorDatabase, limit: int, offset: int):
    cursor = db.books.find().skip(offset).limit(limit)
    books = []
    async for document in cursor:
        document["_id"] = str(document["_id"]) 
        books.append(document)
    return books

async def add(db: AsyncIOMotorDatabase, book_data: dict):
    result = await db.books.insert_one(book_data)
    book_data["_id"] = str(result.inserted_id)
    return book_data