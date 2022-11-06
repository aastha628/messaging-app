from fastapi import FastAPI, Response
from models.agent import Agent
from models.response import ResponseModel
from repository.agent import AgentRepository
from repository.query import QueryRepository
from repository.response import ResponseRepo

app = FastAPI()


@app.post("/register")
async def register(agent: Agent, res: Response):
    return AgentRepository().registerUser(agent, res)


@app.get("/message")
def getResponse(res: Response):
    return QueryRepository().getquery(res)


@app.post("/response")
async def postResponse(response: ResponseModel, res: Response):
    return ResponseRepo().storeResponse(response, res)


@app.get("/")
def read_root():
    return {'message': "Welcome to messaging app!"}
