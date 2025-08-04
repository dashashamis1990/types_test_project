
from typing import List, Optional
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float
    tags: Optional[List[str]] = []