from typing import Union
from pydantic import BaseModel

class ResponseModel(BaseModel):
    r_id:Union[int,None]=None
    query_id:int
    agent_id:int
    response:str