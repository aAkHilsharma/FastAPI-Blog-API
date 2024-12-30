from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    body: str

class BlogResponse(Blog):
    class Config:
        from_attributes = True