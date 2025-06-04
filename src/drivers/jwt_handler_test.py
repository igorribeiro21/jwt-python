from .jwt_handler import JwtHandler

def test_jwt_handler():
    jwt_hander = JwtHandler()
    body = {
        "username": "teste",
    }

    token = jwt_hander.create_jwt_token(body)
    token_information = jwt_hander.decode_jwt_token(token)

    assert token is not None
    assert isinstance(token, str)
    assert token_information["username"] == body["username"]