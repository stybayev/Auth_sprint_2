from http import HTTPStatus
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, Path, HTTPException, Request

from app.models.base_model import SearchParams
from app.models.genre import Genre, Genres
from app.services.genres import GenreServiceABC
from app.utils.dc_objects import PaginatedParams
from app.core.tracer import traced

router = APIRouter()


@router.get("/{genre_id}", response_model=Genre)
@traced(__name__)
async def get_genre(
        request: Request,
        service: GenreServiceABC = Depends(),
        genre_id: UUID = Path(..., description="genre id")
) -> Genre or None:
    genre = await service.get_by_id(doc_id=genre_id)
    if not genre:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="genre not found"
        )
    return genre


@router.get("/", response_model=List[Genres])
@traced(__name__)
async def get_genres(
        request: Request,
        service: GenreServiceABC = Depends(),
        page_size: int = PaginatedParams.page_size,
        page_number: int = PaginatedParams.page_number
) -> List[Genres]:
    genres = await service.get_genres(
        params=SearchParams(
            page_size=page_size,
            page_number=page_number
        )
    )
    return genres
