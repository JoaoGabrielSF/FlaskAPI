from datetime import datetime


class Validator:
    def validate_type(self, element, desired_type):
        # Dictionary to map desired types to validation functions
        type_validators = {
            "int": lambda x: isinstance(x, int),
            "string": lambda x: isinstance(x, str),
            "datetime": lambda x: isinstance(x, datetime),
            "float": lambda x: isinstance(x, float),
            "list": lambda x: isinstance(x, list),
        }

        # Validate based on desired type
        if isinstance(desired_type, list):
            return element in desired_type
        elif desired_type in type_validators:
            return type_validators[desired_type](element)
        else:
            raise ValueError("Invalid value for desired type")

    def validateTypes(self, element, fields):
        # Validate types of fields in the element
        for field, desired_type in fields.items():
            if field in element:
                if not self.validate_type(element[field], desired_type):
                    return False
        return True

    def validate(self, element, fields, required_fields, optional_fields):
        # Validate field types
        if not self.validateTypes(element, fields):
            raise ValueError("Invalid type of field")

        element_fields = set(element.keys())
        required_fields = set(required_fields)
        optional_fields = set(optional_fields)

        # Check for missing required fields
        if len(required_fields - element_fields) > 0:
            raise ValueError("Required field missing")

        # Check for invalid fields in the element
        if len(element_fields - (required_fields | optional_fields)) > 0:
            raise ValueError("Invalid field in element")


class UserNotFoundException(Exception):
    pass

    def user_exists(id, query):
        if query is None:
            raise UserNotFoundException("The User Doesn't Exist")
        else:
            return True
