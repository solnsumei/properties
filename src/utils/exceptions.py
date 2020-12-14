from fastapi import HTTPException, status


def unauthorised_exception(message: str = None) -> HTTPException:
    return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=message or "Please provide authorization token",
            headers={"WWW-Authenticate": "Bearer"},
        )


def login_exception() -> HTTPException:
    return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username and/or password is incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )
