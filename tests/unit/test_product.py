import pytest
from unittest.mock import patch
from flask_restx import Namespace, Resource, fields, Model
from flask_jwt_extended import create_access_token

from app import create_app
from apis import api

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.app_context():
        with app.test_client() as client:        
            yield client

@pytest.fixture
def headers():
    token = create_access_token("testuser")
    return {"Authorization": f"Bearer {token}"}
# def test_demo():
#     assert True