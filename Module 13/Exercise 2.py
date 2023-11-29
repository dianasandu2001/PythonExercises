import json

from flask import Flask, Response

app = Flask(__name__)

import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='dianapass',
    autocommit=True
)
@app.route('/airport/<ICAO_code>')
def airport(ICAO_code):
    try:
        cursor = connection.cursor()
        statement = "select name, municipality from airport where ident = '" + ICAO_code + "'"
        cursor.execute(statement)
        result = cursor.fetchall()
        for i in result:
            print("The name of the airport is " + i[0] + " and it is located in the Town, " + i[1])
            response = {
                "Name" : i[0],
                "Location" : i[1],
                "status" : 200
            }
            return response
    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)