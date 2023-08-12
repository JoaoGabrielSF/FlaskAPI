from flask import Flask, request, json
from datetime import datetime
from src.view.views import UserViewSet


app = Flask(__name__)
user_viewset = UserViewSet()


@app.route("/api/v1/user/user_create", methods=["POST"])
def create_user():
    data = request.get_json()
    data["created"] = datetime.today()

    response = app.response_class(
        response=json.dumps(
            {
                "message": "User created successfully",
                "inserted_id": user_viewset.create(data),
                "created_in": datetime.today().strftime("%c"),
            }
        ),
        status=201,
        mimetype="application/json",
    )
    return response


@app.route("/api/v1/users/", methods=["GET"])
def list_user():
    response = app.response_class(
        response=user_viewset.find(), status=200, mimetype="application/json"
    )
    return response


@app.route("/api/v1/user/<int:user_id>/user_retrieve/", methods=["GET"])
def retrieve_user(user_id):
    response = app.response_class(
        response=json.dumps(user_viewset.find_by_id(user_id)),
        status=200,
        mimetype="application/json",
    )
    return response


@app.route("/api/v1/user/<int:user_id>/user_delete", methods=["DELETE"])
def delete_user(user_id):
    response = app.response_class(
        response=json.dumps(user_viewset.delete(user_id)),
        status=200,
        mimetype="application/json",
    )
    return response


@app.route("/api/v1/user/<int:user_id>/user_update", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    data["updated"] = datetime.today()

    response = app.response_class(
        response=json.dumps(user_viewset.update(user_id, data)),
        status=200,
        mimetype="application/json",
    )
    return response


if __name__ == "__main__":
    app.run()
