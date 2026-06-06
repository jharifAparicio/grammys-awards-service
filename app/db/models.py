# app/bd/models.py
from datetime import datetime
from sqlmodel import SQLModel, Field


class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: int | None = Field(default=None, primary_key=True)

    name: str = Field(
        max_length=100,
        unique=True,
        index=True
    )

    description: str | None = Field(
        default=None,
        max_length=500
    )

    is_active: bool = Field(default=True)

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )