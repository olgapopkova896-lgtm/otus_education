from pydantic import BaseModel, TypeAdapter
from typing import Literal


class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: str | None = None
    address_1: str | None = None
    address_2: str | None = None
    address_3: str | None = None
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: float | None = None
    latitude: float | None = None
    phone: str | None = None
    website_url: str | None = None
    state: str
    street: str | None = None

