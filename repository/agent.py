from fastapi import Response, status
from dbConnection import Database
from models.agent import Agent
from utils.jsonFormatter import getJsonResponse


class AgentRepository:

    def __init__(self):
        self.connection = Database.getInstance()
        self.cur = self.connection.cursor()
        self.table_name = "agents"

    def registerUser(self, agent: Agent, res: Response):
        try:
            record_to_insert = (agent.email, agent.password)
            query = """insert into agents (email,password) values(%s,%s) returning *"""
            self.cur.execute(query, record_to_insert)
            result = getJsonResponse(self.cur)
            self.connection.commit()
            return result
        except Exception as e:
            res.status_code = status.HTTP_400_BAD_REQUEST
            self.connection.rollback()
            return {"error": str(e)}
    
    def checkValidAgent(self,agent_id:int):
        try:
            print(agent_id)
            query="""select exists (select * from agents where agent_id = %s)"""
            self.cur.execute(query,[agent_id])
            result=getJsonResponse(self.cur)
            self.connection.commit()
            return result
        except Exception as e:
            self.connection.rollback()
            return {"error": str(e)}
