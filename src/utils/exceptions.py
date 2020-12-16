from fastapi import HTTPException, status


class UnauthorisedException(HTTPException):
    """Exception raised for authorization errors.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = None):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=message or "Please provide authorization token",
            headers={"WWW-Authenticate": "Bearer"}
        )

