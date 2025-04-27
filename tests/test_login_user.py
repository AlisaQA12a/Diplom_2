import allure
import pytest
import requests

from data import DataMessage
from helpers import generate_password, generate_email
from urls import Urls


class TestUserLogin:
    @allure.title("Авторизация существующего пользователя")
    @allure.description("Передаем данные существующего пользователя")
    def test_user_login(self, create_and_delete_user):
        user_data, response_data = create_and_delete_user
        email, password, name = user_data
        params = {
            "email": email,
            "password": password,
        }
        response = requests.post(
            Urls.LOGIN_USER,
            json=params,
        )
        login_data = response.json()
        assert response.status_code == 200 and login_data["success"]

    @allure.title("Авторизация несуществующего пользователя")
    @allure.description(
        "Передаем по очереди передаем невалидные данные в паре с валидными."
    )
    @pytest.mark.parametrize(
        "params",
        [
            {
                "email": "ValidUser.email",
                "password": generate_password(),
            },
            {
                "email": generate_email(),
                "password": "ValidUser.password",
            },
        ],
    )
    def test_user_login_with_invalid_params(self, params):
        response = requests.post(
            Urls.LOGIN_USER,
            json=params,
        )
        assert response.status_code == 401 and response.json() == DataMessage.MESSAGE_EMAIL_OR_PASSWORD_ARE_INCORRECT