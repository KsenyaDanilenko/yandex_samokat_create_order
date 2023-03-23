import sender_stand_request
import data


#Функция для позитивной проверки создания заказа и получения заказа по order_id
def positive_assert():
    # В переменную current_body копируем данные для создания заказа из словаря data
    current_body = data.order_body.copy()
    # В переменную order_response сохраняем результат запроса на создание заказа:
    order_response = sender_stand_request.post_new_order(current_body)
    response_body = order_response.json()
    # В переменную order_id сохраняем id созданного заказа:
    order_id = order_response.json()["track"]
    # В переменную get_order_response сохраняем результат запроса заказа по id
    get_order_response = sender_stand_request.get_order_by_id(order_id)

    print(response_body)
    print(get_order_response.text)

    # Проверяется, что код ответа равен 201
    assert order_response.status_code == 201
    # Проверяется, что в ответе есть поле authToken, и оно не пустое
    assert order_response.json()["track"] != ""

    assert get_order_response.status_code == 200



#Вызов функции
def test_create_order_success_response():
   positive_assert()
