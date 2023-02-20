from typing import Optional
from pydantic import BaseModel


class Sample(BaseModel):
    id: Optional[int]

    name: str
    number: 
