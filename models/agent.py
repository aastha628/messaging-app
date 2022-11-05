from typing import Union
from pydantic import BaseModel

class Agent(BaseModel):
    id:Union[int,None]=None
    email:str
    password:str