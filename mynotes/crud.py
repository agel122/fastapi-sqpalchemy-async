from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select

from . import models, schemas


async def create_author(db: AsyncSession, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    await db.flush()


async def create_record(db: AsyncSession, record: schemas.RecordCreate):
    db_record = models.Record(expired_at=record.expired_at,
                              description=record.description,
                              author_id=record.author_id)
    db.add(db_record)
    await db.flush()


async def get_record(db: AsyncSession, record_id: int):
    result = await db.execute(select(models.Record).where(models.Record.id == record_id))
    return result.scalars().first()


async def get_records(db: AsyncSession, author_id: int) -> list[models.Record]:
    result = await db.execute(select(models.Record).where(models.Record.author_id == author_id))
    return result.scalars().all()


async def delete_record(db: AsyncSession, record_id: int):
    await db.execute(delete(models.Record).where(models.Record.id == record_id))


async def delete_author(db: AsyncSession, author_id: int):
    await db.execute(delete(models.Author).where(models.Author.id == author_id))
