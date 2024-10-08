from pydantic import BaseModel, Field
from uuid import uuid4


class Like(BaseModel):
    movie_id: str = Field(default_factory=lambda: str(uuid4()))
    rating: int = Field(..., ge=0, le=10)


class MovieLikesResponse(BaseModel):
    likes: int
    dislikes: int


class MovieRatingResponse(BaseModel):
    average_rating: float | None
