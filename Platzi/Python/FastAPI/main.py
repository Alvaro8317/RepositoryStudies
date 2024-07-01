from enum import Enum
from fastapi import FastAPI, Body, Path, Query, status, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import HTTPBearer
from pydantic import BaseModel, Field
from typing import List
from jwt_manager import create_token, validate_token
from config.database import Session, engine, Base
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()
app.title = 'Web App with FastAPI'
app.version = '0.1'
Base.metadata.create_all(bind=engine)
email_admin = "admin@hotmail.com"


# movies: list = [{
#     "id": 1,
#     "title": "Avatar",
#     "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
#     "year": "2009",
#     "rating": 7.8,
#     "category": "Acción"
# }, {
#     "id": 2,
#     "title": "Avatar",
#     "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
#     "year": "2009",
#     "rating": 7.8,
#     "category": "Acción"
# }, {
#     "id": 3,
#     "title": "Halloween Kills",
#     "overview": "Es una película de terror dirigida por David Gordon Green y escrita por Green,
#     Danny McBride y Scott Teems. Se trata de una secuela directa de Halloween y la duodécima
#     entrega de la franquicia Halloween.",
#     "year": "2021",
#     "rating": 7.8,
#     "category": "Terror"
# }]


class Category(str, Enum):
    accion = "Acción"
    terror = "Terror"
    suspenso = "Suspenso"


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["email"] != email_admin:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


class Movie(BaseModel):
    id: int | None = None
    # title: str = Field(min_length=5, max_length=15, default="A movie of reference") Con default dentro
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


class User(BaseModel):
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=5, max_length=50)


@app.get("/", tags=['Home'], status_code=status.HTTP_200_OK)
def message():
    return {"message": "Hello World from FastAPI"}


@app.get("/html", tags=['Home'], status_code=status.HTTP_200_OK)
def message_html():
    return HTMLResponse('<h1>Hello world</h1>')


@app.get("/movies", tags=['Movies'], response_model=List[Movie], status_code=status.HTTP_200_OK,
         dependencies=[Depends(JWTBearer())])
def get_movies() -> JSONResponse:
    db = Session()
    result = db.query(MovieModel).all()
    # return JSONResponse(content=movies)
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


# Parametros de ruta
@app.get("/movies/{id}", tags=['Movies'], response_model=Movie, status_code=status.HTTP_200_OK)
def get_movie(id: int = Path(ge=1, le=2000)) -> JSONResponse:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(content={"message": "Movie not found"}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
    # movie = [movie for movie in movies if movie["id"] == id]
    # if not movie:
    #     return JSONResponse(content=[], status_code=status.HTTP_404_NOT_FOUND)
    # return JSONResponse(content=movie)


# Parametros de Query, son clave y valor
@app.get("/movies/", tags=['Movies'], response_model=List[Movie], status_code=status.HTTP_200_OK)
def get_movies_by_category(category: str = Query(min_length=3, max_length=15),
                           year: int = Query(ge=1900, le=2024)) -> JSONResponse:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.category == category).filter(MovieModel.year == year).all()
    if not result:
        return JSONResponse(content={"message": "No se encontraron películas con esas características"},
                            status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
    # movies_to_find = [movie for movie in movies if movie["category"] == category and movie["year"] == str(year)]
    # if not movies_to_find:
    #     return JSONResponse(content="No se encontraron películas con esas características",
    #                         status_code=status.HTTP_404_NOT_FOUND)
    # return JSONResponse(content=movies_to_find)


@app.post("/movies", tags=['Movies'], response_model=dict, status_code=status.HTTP_201_CREATED)
# Esta no es la forma ideal, mejor tener un modelo
def post_movie(movie: Movie):
    db = Session()
    new_movie = MovieModel(**movie.model_dump())
    db.add(new_movie)
    db.commit()
    # movies.append(movie.model_dump())
    return JSONResponse(content={"Message": "Se ha registrado la película"})


@app.put("/movies/{id}", tags=['Movies'], response_model=dict, status_code=status.HTTP_200_OK)
def update_movie(id: int, new_movie_to_update: Movie):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(content={"Message": f"Película no encontrada con el ID {id}"},
                            status_code=status.HTTP_404_NOT_FOUND)
    result.title = new_movie_to_update.title
    result.overview = new_movie_to_update.overview
    result.year = new_movie_to_update.year
    result.rating = new_movie_to_update.rating
    result.category = new_movie_to_update.category
    db.commit()
    return JSONResponse(content={"Message": "Se ha modificado la película"})
    # for movie in movies:
    #     if movie["id"] == id:
    #         movie["title"] = new_movie_to_update.title
    #         movie["overview"] = new_movie_to_update.overview
    #         movie["year"] = str(new_movie_to_update.year)
    #         movie["rating"] = new_movie_to_update.rating
    #         movie["category"] = new_movie_to_update.category
    #         return JSONResponse(content={"Message": "Se ha modificado la película"})
    # return JSONResponse(content={"Message": f"Película no encontrada con el ID {id}"},
    #                     status_code=status.HTTP_404_NOT_FOUND)


@app.delete("/movies/{id}", tags=['Movies'], response_model=dict, status_code=status.HTTP_200_OK)
def delete_movie(id: int):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(content={"Message": f"Película no encontrada con el ID {id}"},
                            status_code=status.HTTP_404_NOT_FOUND)
    db.delete(result)
    db.commit()
    return JSONResponse(content={"Message": "Se ha eliminado la película"})
    # for movie in movies:
    #     if movie["id"] == id:
    #         movies.remove(movie)
    #         return JSONResponse(content={"Message": "Se ha eliminado la película"})
    # return JSONResponse(content={"Message": f"Película no encontrada con el ID {id}"},
    #                     status_code=status.HTTP_404_NOT_FOUND)


@app.post("/login", tags=['Login'], response_model=dict, status_code=status.HTTP_201_CREATED)
def login_user(user: User) -> JSONResponse:
    if user.email == email_admin and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(content={"Token": token})
    return JSONResponse(content={"Message": "Invalid Credentials"}, status_code=status.HTTP_401_UNAUTHORIZED)
