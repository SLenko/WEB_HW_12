from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.api.users import crud as user_crud

router = APIRouter()
security = HTTPBasic()

@router.post("/login")
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    user = user_crud.authenticate_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return {"access_token": user_crud.create_access_token(user.email)}
