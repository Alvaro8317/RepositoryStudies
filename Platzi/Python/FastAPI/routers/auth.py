from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from config.database import email_admin
from utils.jwt_manager import create_token
from schemas.user import User

router = APIRouter()


@router.post("/login", tags=['Login'], response_model=dict, status_code=status.HTTP_201_CREATED)
def login_user(user: User) -> JSONResponse:
    if user.email == email_admin and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(content={"Token": token})
    return JSONResponse(content={"Message": "Invalid Credentials"}, status_code=status.HTTP_401_UNAUTHORIZED)
