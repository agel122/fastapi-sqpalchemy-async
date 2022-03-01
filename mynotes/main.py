import uvicorn
from fastapi import FastAPI

from database import engine, Base
from . import routers

app = FastAPI()
app.include_router(routers.router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__=="__main__":
    uvicorn.run("app:app", port=1111, host='127.0.0.1')

