import allure
import pytest
import requests

from data import DataMessage, ValidUser
from urls import Urls
from helpers import generate_username, generate_email, generate_password

class TestCreateUser:
    @allure.title("Создание пользователя")
    @allure.description("Передаем все обязательные поля")
    def test_create_user(self):
        payload = {
            "email": generate_email(),
            "password": generate_password(),
            "name": generate_username(),
        }
        response = requests.post(
            Urls.CREATE_USER,
            json=payload,
        )
        data = response.json()
        assert response.status_code == 200 and data["success"]

    @allure.title("Получение ошибки при создании существующего пользователя")
    @allure.description("Передаем данные существующего пользователя")
    def test_create_same_user(self):
        payload = {
            "email": ValidUser.email,
            "password": ValidUser.password,
            "name": ValidUser.name,
        }
        response = requests.post(
            Urls.CREATE_USER,
            json=payload,
        )
        assert response.status_code == 403 and response.json() == DataMessage.MESSAGE_USER_ALREADY_EXISTS

    @allure.title("Получение ошибки при создании пользователя без одного из обязательных полей")
    @allure.description("По очереди не передаем одно из обязательных полей")
    @pytest.mark.parametrize(
        "params",
        [
            {
                "email": generate_email(),
                "password": generate_email(),
                "name": "",
            },
            {
                "email": "",
                "password": generate_password(),
                "name": generate_password(),
            },
            {
                "email": generate_username(),
                "password": "",
                "name": generate_username(),
            },
        ],
    )
    def test_create_user_without_one_of_required_fields(self, params):
        response = requests.post(
            Urls.CREATE_USER,
            json=params,
        )
        assert response.status_code == 403 and response.json() == DataMessage.MESSAGE_ONE_OF_THE_FIELDS_IS_EMPTY
