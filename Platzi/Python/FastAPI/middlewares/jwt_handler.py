from fastapi import status, Request, HTTPException
from fastapi.security import HTTPBearer

from utils.jwt_manager import validate_token
from config.database import email_admin


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["email"] != email_admin:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
