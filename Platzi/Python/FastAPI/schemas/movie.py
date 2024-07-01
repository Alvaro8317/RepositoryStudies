from pydantic import BaseModel, Field
from schemas.category import Category


class Movie(BaseModel):
    id: int | None = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: str | int = Field(le=2025)
    rating: float = Field(gt=1, le=10)
    category: Category

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "El cuervo",
                "overview": "Es una buena película",
                "year": "1997",
                "rating": 8.0,
                "category": "Suspenso"
            }
        }
