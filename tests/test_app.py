from tests import client


def test_get_test(client):
    response = client.get('/')
    assert response.status_code == 404
