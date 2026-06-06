#app/db/database.py
from sqlmodel import SQLModel, create_engine

from app.core.config import DATABASE_URL
from app.db.models import Category, Candidate

engine = create_engine(
    DATABASE_URL,
    echo=True
)

def create_db():
    SQLModel.metadata.create_all(engine)