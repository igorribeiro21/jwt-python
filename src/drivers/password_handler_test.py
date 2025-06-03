from .password_handler import PasswordHandler

def test_encrypt():
    my_password = "123Rocket"
    password_handelr = PasswordHandler()
    
    hashed_password = password_handelr.encrypt_password(my_password)

    password_checked = password_handelr.check_password(my_password, hashed_password)

    assert password_checked
