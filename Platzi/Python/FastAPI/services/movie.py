from models.movie import Movie as MovieModel
from config.database import Session
from schemas.movie import Movie


class MovieService():
    def __init__(self, db) -> None:
        self.db: Session = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result

    def get_movie(self, movie_id):
        result = self.db.query(MovieModel).filter(MovieModel.id == movie_id).first()
        return result

    def get_movies_by_category_and_year(self, category, year):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).filter(MovieModel.year == year).all()
        return result

    def create_movie(self, movie: Movie) -> None:
        new_movie = MovieModel(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return

    def update_movie(self, id_movie: int, movie_new: Movie) -> bool:
        result = self.get_movie(id_movie)
        if not result:
            return False
        result.title = movie_new.title
        result.overview = movie_new.overview
        result.year = movie_new.year
        result.rating = movie_new.rating
        result.category = movie_new.category
        self.db.commit()
        return True

    def delete_movie(self, movie):
        self.db.delete(movie)
        self.db.commit()
