from sqlalchemy.orm import Session
from sqlalchemy import delete

from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item



async def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    await db.flush()

async def create_record(db: Session, record: schemas.RecordCreate):
    db_record = models.Record(expired_at=record.expired_at,
                              description=record.description,
                              author_id=record.author_id)
    db.add(db_record)
    await db.flush()

async def update_record(db: Session, record: schemas.RecordCreate):

async def get_record(db: Session):

async def get_records(db: Session):

async def delete_record(db: Session, record_id: int):
    await db.execute(delete(models.Record).where(models.Record.id == record_id))

async def delete_author(db: Session, author_id: int):
    await db.execute(delete(models.Author).where(models.Author.id == author_id))