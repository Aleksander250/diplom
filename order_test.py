# Александр Страхов, 24-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_create_order_success_response():
    order_response = sender_stand_request.create_order()
    track_number = order_response.json()["track"]
    order_by_number_response = sender_stand_request.get_track_order(track_number)
    assert order_by_number_response.status_code == 200, "Статус код не равен 200"



