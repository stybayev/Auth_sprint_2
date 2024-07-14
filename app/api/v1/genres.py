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
    """
    ## Получение информации о жанре

    Этот эндпоинт позволяет получить подробную информацию о жанре по его уникальному идентификатору.

    ### Параметры:
    - **genre_id**: Уникальный идентификатор жанра.

    ### Возвращает:
    - Объект жанра с подробной информацией.
    - Если жанр не найден, возвращает ошибку `404 Not Found`.
    """
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
    """
    ## Получение списка жанров

    Этот эндпоинт позволяет получить список жанров с возможностью пагинации.

    ### Параметры:
    - **page_size**: Количество жанров на странице (по умолчанию: `10`).
    - **page_number**: Номер страницы (по умолчанию: `1`).

    ### Возвращает:
    - Список жанров с информацией о каждом жанре.
    """
    genres = await service.get_genres(
        params=SearchParams(
            page_size=page_size,
            page_number=page_number
        )
    )
    return genres
