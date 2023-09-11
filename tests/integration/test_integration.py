from tests.test_config import client

integration_data = {
    "imei": "string",
    "serial": "string",
    "momsn": "string",
    "transmit_time": "2023-05-19T07:04:05.319Z",
    "iridium_latitude": "string",
    "iridium_longitude": "string",
    "iridium_cep": 0,
    "data": "string"
}


def test_get_empty_integration_data():
    response = client.get(f"/integration/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_integration_data():
    response = client.post(f"/integration/", json=integration_data)
    assert response.status_code == 200
