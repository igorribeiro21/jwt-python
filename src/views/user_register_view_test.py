import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .user_register_view import UserRegisterView

class MockController:
    def registry(self, username, password):
        return {
            "count": 1,
            "username": username
        }

def test_handle_user_register():
    body = {
        "username": "myusername",
        "password": "myPassword",
    }

    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    response = user_register_view.handle(request)
    
    assert isinstance(response, HttpResponse)
    assert response.body == {'data': {'count': 1, 'username': 'myusername'}}
    assert response.status_code == 201

def test_handle_user_register_with_validation_error():
    body = {
        "password": "myPassword",
    }

    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
        user_register_view.handle(request)
