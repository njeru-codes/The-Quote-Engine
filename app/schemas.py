from pydantic import BaseModel
from typing import Optional

class Quote(BaseModel):
    quote: str
    author: Optional[str]=None