from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends
from fastapi.security import HTTPBearer
from config import Config
from src.models.models import User
from .exceptions import unauthorised_exception


async def authenticate(email: str, password: str):
    user = await User.find_by_email(email)

    if user and User.verify_hash(password, user.password):
        return user


def check_token(auth_token=Depends(HTTPBearer(
    scheme_name="auth",
    bearerFormat="Bearer",
    auto_error=False,
))):
    """
    Check valid token
    :param auth_token:
    :return: str
    """
    if auth_token is None:
        raise unauthorised_exception()

    try:
        payload = jwt.decode(
            auth_token.credentials,
            Config.SECRET_KEY,
            algorithms=[Config.ALGORITHM]
        )

        username: str = payload.get("sub")
        if username is None:
            raise JWTError
    except JWTError:
        raise unauthorised_exception(
            message="Invalid token"
        )
    return username


async def get_current_user(username: str = Depends(check_token)):
    """
    Fetch logged in user from database
    :param username:
    :return: User
    """
    user = await User.find_by_email(email=username)
    if user is None:
        raise unauthorised_exception(
            message="Invalid token"
        )
    return user


def create_token(data: dict, expiry: Optional[timedelta] = None):
    to_encode = data.copy()

    if expiry:
        expire = datetime.utcnow() + expiry
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)

    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, Config.SECRET_KEY, algorithm=[Config.ALGORITHM])

    return token
