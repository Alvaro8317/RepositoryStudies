from typing import List
from fastapi import APIRouter, Depends, Path, Query, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from middlewares.jwt_handler import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

router = APIRouter()


@router.get("/movies", tags=['Movies'], response_model=List[Movie], status_code=status.HTTP_200_OK,
            dependencies=[Depends(JWTBearer())])
def get_movies() -> JSONResponse:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.get("/movies/{id_movie}", tags=['Movies'], response_model=Movie, status_code=status.HTTP_200_OK)
def get_movie(id_movie: int = Path(ge=1, le=2000)) -> JSONResponse:
    db = Session()
    print("Entró al router")
    result = MovieService(db).get_movie(id_movie)
    if not result:
        return JSONResponse(content={"message": "Movie not found"}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.get("/movies/", tags=['Movies'], response_model=List[Movie], status_code=status.HTTP_200_OK)
def get_movies_by_category(category: str = Query(min_length=3, max_length=15),
                           year: int = Query(ge=1900, le=2024)) -> JSONResponse:
    db = Session()
    result = MovieService(db).get_movies_by_category_and_year(category, year)
    if not result:
        return JSONResponse(content={"message": "No se encontraron películas con esas características"},
                            status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.post("/movies", tags=['Movies'], response_model=dict, status_code=status.HTTP_201_CREATED)
def post_movie(movie: Movie):
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"Message": "Se ha registrado la película"})


@router.put("/movies/{id_movie}", tags=['Movies'], response_model=dict, status_code=status.HTTP_200_OK)
def update_movie(id_movie: int, new_movie_to_update: Movie):
    db = Session()
    result: bool = MovieService(db).update_movie(id_movie, new_movie_to_update)
    if not result:
        return JSONResponse(content={"Message": f"Película no encontrada con el ID {id_movie}"},
                            status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"Message": "Se ha modificado la película"})


@router.delete("/movies/{id_movie}", tags=['Movies'], response_model=dict, status_code=status.HTTP_200_OK)
def delete_movie(id_movie: int):
    db = Session()
    movie_service = MovieService(db)
    movie_result = movie_service.get_movie(id_movie)
    if not movie_result:
        return JSONResponse(content={"Message": f"Película no encontrada con el ID {id_movie}"},
                            status_code=status.HTTP_404_NOT_FOUND)
    movie_service.delete_movie(movie_result)
    return JSONResponse(content={"Message": "Se ha eliminado la película"})
