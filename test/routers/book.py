from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/book",
    tags=["Book"],
    responses={404: {"message": "Not found"}}
)

book_db = [
    {
        "title":"test1",
        "price": 100,
        "id": 0
    }
]

class Book(BaseModel):
    title: str
    price: float
    book_id: int

@router.get("")
async def get_books():
    return book_db

@router.get("/{book_id}")
async def get_book(book_id: int):
    return book_db[book_id]


@router.post("")
async def create_book(book: Book):
    book_db.append(book.dict())
    return book_db[-1]

@router.put("/{book_id}")
async def edit_book(book_id: int, book: Book):
    result = book.dict()
    book_db[book_id].update(result)
    return result

@router.delete("/{book_id}")
async def delete_book(book_id: int):
    book = book_db.pop(book_id)
    return book