import json


def getJsonResponse(cur, many=False):
    row_headers = [x[0] for x in cur.description]
    json_data = []
    if many:
        result = cur.fetchall()
        for r in result:
            json_data.append(dict(zip(row_headers, r)))
    else:
        result = cur.fetchone()
        json_data = dict(zip(row_headers, result))
    return json_data
