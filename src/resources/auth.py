from fastapi import Depends
from .baserouter import APIRouter
from src.models.schema.schema import AuthSchema
from src.utils.security import create_token, authenticate, get_current_user
from src.models.models import UserPydantic


router = APIRouter()


@router.post('/login')
async def login_user(auth: AuthSchema):
    found_user = await authenticate(auth.email, auth.password)
    token = create_token({"sub": found_user.email})
    user_pydantic = await UserPydantic.from_tortoise_orm(found_user)

    return {
        "user": user_pydantic,
        "token": token
    }


@router.get('/user')
async def profile(user: dict = Depends(get_current_user)):
    logged_in_user = await UserPydantic.from_tortoise_orm(user)
    return {
        "user": logged_in_user,
    }

