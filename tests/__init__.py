from app import app
import pytest


@pytest.fixture
def client(scope='session'):
    app.testing = True
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client
    
    # free variables, files and sessions
