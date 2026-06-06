# app/bd/models.py
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

# Category model
class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(
        max_length=100,
        unique=True,
        index=True
    )

    description: Optional[str] = Field(
        default=None,
        max_length=500
    )

    is_active: bool = Field(default=True)

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    candidates: List["Candidate"] = Relationship(
        back_populates="category"
    )

# Candidate model
class Candidate(SQLModel, table=True):
    __tablename__ = "candidates"

    id: int | None = Field(default=None, primary_key=True)

    name: str = Field(
        max_length=150,
        index=True
    )

    biography: str | None = Field(
        default=None,
        max_length=1000
    )

    image_url: str | None = Field(
        default=None,
        max_length=500
    )

    is_active: bool = Field(default=True)

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    category_id: int = Field(
        foreign_key="categories.id"
    )

    category: Optional["Category"] = Relationship(
        back_populates="candidates"
    )