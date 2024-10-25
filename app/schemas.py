from pydantic import BaseModel
from typing import Optional

class LinkCreate(BaseModel):
    url: str

class Link(BaseModel):
    id: int
    url: str
    short_code: str
