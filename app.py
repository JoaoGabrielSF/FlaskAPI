from flask import Flask
from flask import json

app = Flask(__name__)

@app.route('/api/v1/user/user_create')
def create_user():
    response = app.response_class(
        response=json.dumps("This is an example app test"),
        status=200,
        mimetype='application/json'
    )
    return response


def retrieve_user():
    response = app.response_class(
        response=json.dumps("This is an example app test"),
        status=200,
        mimetype='application/json'
    )
    return response

def delete_user():
    response = app.response_class(
        response=json.dumps("This is an example app test"),
        status=200,
        mimetype='application/json'
    )
    return response