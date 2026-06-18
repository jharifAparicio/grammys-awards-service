# app/db/models.py
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship


class Nomination(SQLModel, table=True):
    """Tabla intermedia para la relación Muchos a Muchos entre Categorías y Candidatos."""
    __tablename__ = "nominations"

    category_id: int | None = Field(
        default=None, foreign_key="categories.id", primary_key=True
    )
    candidate_id: int | None = Field(
        default=None, foreign_key="candidates.id", primary_key=True
    )
    # Podemos agregar metadatos de la nominación en el futuro, ej. year: int


# Category model
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
        default_factory=lambda: datetime.now(timezone.utc)
    )

    # Relación muchos a muchos con Candidate a través de Nomination
    candidates: list["Candidate"] = Relationship(
        back_populates="categories", link_model=Nomination
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
        default_factory=lambda: datetime.now(timezone.utc)
    )

    # Relación muchos a muchos con Category a través de Nomination
    categories: list["Category"] = Relationship(
        back_populates="candidates", link_model=Nomination
    )