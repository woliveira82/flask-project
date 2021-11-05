from tests import client


def test_get_test(client):
    response = client.get('/api/v1/tests')
    assert response.status_code == 200
    assert response.data == b'ok'


def test_get_test_wrong_method(client):
    response = client.post('/api/v1/tests')
    assert response.status_code == 405


def test_get_test_params(client):
    response = client.get('/api/v1/test-params?param=var')
    assert response.status_code == 200
    assert response.json == {'param': 'var'}


def test_get_test_params_miss_param(client):
    response = client.get('/api/v1/test-params')
    assert response.status_code == 422
