from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from . import schemas
from database import get_session

router = APIRouter()


@router.get('/record/{record_id}', response_model=schemas.Record)
async def get_record(record_id: int, session: AsyncSession = Depends(get_session)):
    record = await crud.get_record(db=session, record_id=record_id)
    return record


@router.get('/records', response_model=list[schemas.Record])
async def get_records(author_id: int, session: AsyncSession = Depends(get_session)):
    records = await crud.get_records(db=session, author_id=author_id)
    return records


@router.post('/add_record')
async def create_record():
    pass


@router.post('/add_author')
async def create_author():
    pass


@router.delete('/record/{record_id}')
async def delete_record(record_id: int, session: AsyncSession = Depends(get_session)):
    return await crud.delete_record(db=session, record_id=record_id)


@router.delete('/author/{author_id}')
async def delete_author(author_id: int, session: AsyncSession = Depends(get_session)):
    return await crud.delete_author(db=session, author_id=author_id)




