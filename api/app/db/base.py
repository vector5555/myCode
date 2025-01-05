from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# Import all models to ensure they are registered with SQLAlchemy
from app.models.user import User
from app.models.role import Role
from app.models.user_role import UserRole
from app.models.project import Project
from app.models.process import Process
from app.models.task import Task
from app.models.construction_record import ConstructionRecord
from app.models.settlement import Settlement

from contextlib import asynccontextmanager

@asynccontextmanager
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
