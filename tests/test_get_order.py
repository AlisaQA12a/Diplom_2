import allure
import requests
from urls import Urls


class TestReceivingOrders:
    @allure.title("Получение заказа авторизованного пользователя")
    @allure.description("Передается токен пользователя")
    def test_receive_orders_authorized_user(self, create_and_delete_user, create_order):
        auth_token = create_and_delete_user[1]["accessToken"]
        headers = {
            "Authorization": f"{auth_token}",
        }
        response = requests.get(Urls.GET_ORDER, headers=headers)
        data = response.json()
        assert response.status_code == 200 and data["success"] and "orders" in data

    @allure.title("Получение ошибки при попытке получения заказа не авторизованного пользователя")
    def test_receive_orders_unauthorized_user(self):
        response = requests.get(Urls.GET_ORDER)
        data = response.json()
        assert response.status_code == 401 and not data["success"]