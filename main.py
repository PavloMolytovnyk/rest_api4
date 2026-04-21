from fastapi import FastAPI
from api.books import router as books_router

app = FastAPI(title="Library Mongo API")

app.include_router(books_router)

@app.get("/")
async def root():
    return {"message": "API with MongoDB is running", "pagination": "limit-offset"}