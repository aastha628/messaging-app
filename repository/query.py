from fastapi import Response, status
from dbConnection import Database
from utils.jsonFormatter import getJsonResponse


class QueryRepository:

    def __init__(self):
        self.connection = Database.getInstance()
        self.cur = self.connection.cursor()
        self.table_name = "queries"

    def getquery(self, agent_id: int, res: Response):
        try:
            query = """update queries 
            set agent_id = %s where q_id = (select q_id from queries where (q_id not in (select query_id from responses)) and (agent_id is null or agent_id = %s) order by agent_id limit 1) returning *
            """
            self.cur.execute(query, [agent_id,agent_id])
            result = getJsonResponse(self.cur)
            self.connection.commit()
            return result
        except Exception as e:
            res.status_code = status.HTTP_400_BAD_REQUEST
            self.connection.rollback()
            return {'error': str(e)}
