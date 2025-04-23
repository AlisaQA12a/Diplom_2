import allure
import requests

from data import DataMessage, DataIngredients
from urls import Urls


class TestCreateOrder:
    @allure.title("успешное создание заказа авторизованного пользователя")
    @allure.description("При заказе передаем ингредиенты")
    def test_create_order_authorized_user_with_ingredients(self, create_and_delete_user):
        auth_token = create_and_delete_user[1]["accessToken"]
        headers = {
            "Authorization": f"{auth_token}",
        }
        payload = DataIngredients.PAILOAD
        response = requests.post(
            Urls.CREATE_ORDER,
            data=payload,
            headers=headers,
        )
        data = response.json()

        assert response.status_code == 200 and data["success"]

    @allure.title("Получение ошибки при попытке создания заказа авторизованного пользователя без ингридиентов")
    @allure.description("Не передаются ингредиенты")
    def test_create_order_authorized_user_no_ingredients(self, create_and_delete_user):
        auth_token = create_and_delete_user[1]["accessToken"]
        headers = {
            "Authorization": f"{auth_token}",
        }
        payload = {
            "ingredients": [""],
        }
        response = requests.post(
            Urls.CREATE_ORDER,
            data=payload,
            headers=headers,
        )
        data = response.json()

        assert response.status_code == 400 and not data["success"] and  response.json() == DataMessage.MESSAGE_INGREDIENT_IDS_MUST_BE_PROVIDED

    @allure.title("Успешное создание заказа с существующими ингридиентами через неавторизованного пользователя")
    def test_create_order_unauthorized_user_with_ingredients(self):
        payload = DataIngredients.PAILOAD
        response = requests.post(
            Urls.CREATE_ORDER,
            data=payload,
        )
        data = response.json()

        assert response.status_code == 200 and data["success"]

    @allure.title("Получение ошибки при попытке создания заказа без ингридиентов через неавторизованного пользователя")
    def test_create_order_unauthorized_user_no_ingredients(self):
        payload = {
            "ingredients": [""],
        }
        response = requests.post(
            Urls.CREATE_ORDER,
            data=payload,
        )
        data = response.json()

        assert response.status_code == 400 and not data["success"] and  response.json() == DataMessage.MESSAGE_INGREDIENT_IDS_MUST_BE_PROVIDED

    @allure.title("Получение ошибки при создании заказа с несуществующими ингридиентами через авторизованного пользователя")
    def test_create_order_auth_user_with_wrong_hash(self, create_and_delete_user):
        auth_token = create_and_delete_user[1]["accessToken"]
        headers = {"Authorization": f"{auth_token}"}
        payload = DataIngredients.INVALID_PAYLOAD
        response = requests.post(
            Urls.CREATE_ORDER,
            data=payload,
            headers=headers,
        )

        # код ответа в документации и в реальности отличаются (в документации ожидается код 500, а в реальности возвращается 400), поэтому тест фейлится
        assert response.status_code == 500