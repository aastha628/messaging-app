from fastapi import Response, status
from models.response import ResponseModel
from dbConnection import Database
from utils.jsonFormatter import getJsonResponse


class ResponseRepo:
    def __init__(self):
        self.connection = Database.getInstance()
        self.cur = self.connection.cursor()
        self.table_name = "responses"

    def storeResponse(self, response: ResponseModel, res: Response):
        try:
            record_to_insert = (response.query_id,
                                response.agent_id, response.response)
            query = """insert into responses (query_id,agent_id,response) values(%s,%s,%s) returning *"""
            self.cur.execute(query, record_to_insert)
            result = getJsonResponse(self.cur)
            self.connection.commit()
            return result
        except Exception as e:
            res.status_code = status.HTTP_400_BAD_REQUEST
            self.connection.rollback()
            return {'error': str(e)}
