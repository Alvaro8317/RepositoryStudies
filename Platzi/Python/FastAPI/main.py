from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandlerMiddleware
from routers import movie_router, auth_router, basic_router

app = FastAPI()
app.title = 'Web App with FastAPI'
app.version = '0.1'
app.add_middleware(ErrorHandlerMiddleware)
app.include_router(movie_router)
app.include_router(auth_router)
app.include_router(basic_router)
Base.metadata.create_all(bind=engine)
email_admin = "admin@hotmail.com"
