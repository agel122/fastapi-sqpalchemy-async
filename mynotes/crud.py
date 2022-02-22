from sqlalchemy.orm import Session
from sqlalchemy import delete, select

from . import models, schemas


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


async def get_record(db: Session, record_id: int):
    return await db.execute(select(models.Record).where(models.Record.id == record_id)).scalars().first()


async def get_records(db: Session, author_id: int):
    return await db.execute(select(models.Record).where(models.Record.author_id == author_id)).scalars().all()


async def delete_record(db: Session, record_id: int):
    await db.execute(delete(models.Record).where(models.Record.id == record_id))


async def delete_author(db: Session, author_id: int):
    await db.execute(delete(models.Author).where(models.Author.id == author_id))
