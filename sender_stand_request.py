import configuration
import requests
import data


def create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                             json=data.order_body)

def get_track_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_ORDER_PATH, params={'t': track_number})





