from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

class Errors(Enum):
    TECH_ISSUE = 0
    BAD_REQUEST = 1
    NOT_FOUND = 2

class Item(BaseModel):
    id: int
    name: str
    price: float
    tags: Optional[List[str]] = []
    error: Optional[Errors] = None