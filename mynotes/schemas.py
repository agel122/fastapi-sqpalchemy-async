from pydantic import BaseModel
from typing import List
from datetime import date, datetime


class AuthorCreate(BaseModel):
    name: str


class RecordCreate(BaseModel):
    expired_at: date
    description: str
    author_id: int


class Record(RecordCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class Author(AuthorCreate):
    id: int
    records: List[Record] = []

    class Config:
        orm_mode = True
