from src.models.users import User
from src.db.validation import Validator
from src.db.validation import UserNotFoundException
from src.db import database
from pymongo.results import DeleteResult
from bson.json_util import dumps


class UserViewSet:
    def __init__(self):
        self.validator = Validator()
        self.db = database.db
        self.collection = database.collection

        self.fields = {
            "nome": "string",
            "idade": "int",
            "profissao": "string",
            "created": "datetime",
            "updated": "datetime",
        }

        self.create_required_fields = ["nome", "idade"]
        self.create_optional_fields = ["profissao", "pertences", "created"]
        self.update_required_fields = ["nome", "idade"]
        self.update_optional_fields = ["profissao", "pertences", "updated"]

    def get_next_user_id(self):
        user_count = self.collection.count_documents({}) + 1
        return user_count

    def create(self, user):
        self.validator.validate(
            user, self.fields, self.create_required_fields, self.create_optional_fields
        )
        user["_id"] = self.get_next_user_id()
        res = self.collection.insert_one(user)
        return dumps(res.inserted_id)

    def find(self):
        return dumps(self.collection.find({}))

    def find_by_id(self, id):
        try:
            query = self.collection.find_one({"_id": id})
            if UserNotFoundException.user_exists(id, query):
                return query
        except UserNotFoundException as e:
            error_message = {"error": str(e)}
            return error_message

    def delete(self, id):
        try:
            query = self.collection.find_one({"_id": id})
            if UserNotFoundException.user_exists(id, query):
                self.collection.delete_one({"_id": id})
                message = {"message": "User Deleted successfully"}
                return message
        except UserNotFoundException as e:
            error_message = {"error": str(e)}
            return error_message

    def update(self, id, user):
        self.validator.validate(
            user, self.fields, self.update_required_fields, self.update_optional_fields
        )
        self.collection.find_one_and_update({"_id": id}, {"$set": user})
        return self.collection.find_one({"_id": id})
