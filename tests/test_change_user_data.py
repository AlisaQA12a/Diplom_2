import allure
import pytest
import requests

from data import DataMessage
from helpers import generate_username, generate_email, generate_password
from urls import Urls


class TestChangeUserData:
    @allure.title("Изменение данных авторизованного пользователя")
    @allure.description("Передаются все обязательные поля")
    @pytest.mark.parametrize(
        "new_user_data",
        [
            ({"email": generate_email()}),
            ({"password": generate_password()}),
            ({"name": generate_username()}),
        ],
    )
    def test_change_data_of_authorized_user(self, new_user_data, create_and_delete_user):
        auth_token = create_and_delete_user[1]["accessToken"]
        headers = {"Authorization": f"{auth_token}"}
        payload = new_user_data
        response = requests.patch(
            Urls.USER_DATA_CHANGE,
            json=payload,
            headers=headers,
        )
        data = response.json()
        assert response.status_code == 200 and data["success"]

    @allure.title("Проверка изменения данных неавторизованного пользователя")
    @allure.description("передаются все обязательные поля")
    @pytest.mark.parametrize(
        "new_user_data",
        [
            ({"email": generate_email()}),
            ({"password": generate_password()}),
            ({"name": generate_username()}),
        ],
    )
    def test_change_data_of_unauthorized_user(self, new_user_data):
        payload = new_user_data
        response = requests.patch(
            Urls.USER_DATA_CHANGE,
            json=payload,
        )
        data = response.json()

        assert response.status_code == 401 and data == DataMessage.MESSAGE_YOU_SHOULD_BE_AUTHORISED