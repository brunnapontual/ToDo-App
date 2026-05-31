from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import create_tables
from app.routers import tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(title="Todo App", lifespan=lifespan)
app.include_router(tasks.router)
