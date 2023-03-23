import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body,  # тело запроса
                         headers=data.headers)  # заголовки

def get_order_by_id(t):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_ID_PATH,  # подставляем полный url
                         params ={"t": t})  #id заказа
