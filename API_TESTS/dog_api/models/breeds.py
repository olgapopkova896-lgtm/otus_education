from typing import Literal
from pydantic import BaseModel


class DogBreedsResponse(BaseModel):
    message: dict[str, list[str]]
    status: Literal["success"]


class DogSingleImageResponse(BaseModel):
    message: str
    status: Literal["success"]


class DogMultipleImageResponse(BaseModel):
    message: list[str]
    status: Literal["success"]
