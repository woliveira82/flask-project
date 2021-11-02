from tests import client


def test_get_test(client):
    response = client.get('/api/v1/tests')
    assert response.status_code == 200
    assert response.data == b'ok'
