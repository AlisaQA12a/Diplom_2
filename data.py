class ValidUser:
    email = ("fluffy1134@bk.ru",)
    password = ("fluffy1134",)
    name = "fluffy"


class DataMessage:
    # пользователь уже существует
    MESSAGE_USER_ALREADY_EXISTS = {"success": False, "message": "User already exists"}
    # нет одного из полей
    MESSAGE_ONE_OF_THE_FIELDS_IS_EMPTY = {
        "success": False,
        "message": "Email, password and name are required fields",
    }
    # неверные логин или пароль
    MESSAGE_EMAIL_OR_PASSWORD_ARE_INCORRECT = {
        "success": False,
        "message": "email or password are incorrect",
    }
    # изменение данных без авторизации
    MESSAGE_YOU_SHOULD_BE_AUTHORISED = {
        "success": False,
        "message": "You should be authorised",
    }
    #нет ни одного ингридиента
    MESSAGE_INGREDIENT_IDS_MUST_BE_PROVIDED = {
        "success": False,
        "message": "Ingredient ids must be provided",
    }

class DataIngredients:
    PAILOAD = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa72",
            "61c0c5a71d1f82001bdaaa6f",
            "61c0c5a71d1f82001bdaaa6c",
        ]
    }
    INVALID_PAYLOAD = {
            "ingredients": ["61c0c5a71d1f82001bdaaa50"],
    }
