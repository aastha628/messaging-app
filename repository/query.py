from fastapi import Response, status
from dbConnection import Database
from utils.jsonFormatter import getJsonResponse


class QueryRepository:

    def __init__(self):
        self.connection = Database.getInstance()
        self.cur = self.connection.cursor()
        self.table_name = "queries"

    def getquery(self,res:Response):
        try:
            query = """select * from queries where id not in (select query_id from responses) limit 1"""
            self.cur.execute(query)
            result = getJsonResponse(self.cur)
            self.connection.commit()
            return result
        except Exception as e:
            res.status_code=status.HTTP_400_BAD_REQUEST
            self.connection.rollback()
            return {'error':str(e)}
