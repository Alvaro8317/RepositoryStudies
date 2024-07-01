from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", tags=['Home'], status_code=status.HTTP_200_OK)
def message():
    return {"message": "Hello World from FastAPI"}


@router.get("/html", tags=['Home'], status_code=status.HTTP_200_OK)
def message_html():
    return HTMLResponse('<h1>Hello world</h1>')
