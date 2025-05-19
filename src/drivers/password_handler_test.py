from .password_handler import PasswordHandler

def test_password_handler():
    password_handler = PasswordHandler()
    password = "minha_senha"

    hash_pwd = password_handler.encrypt_password(password)
    check = password_handler.check_password(password, hash_pwd)

    assert hash_pwd is not None
    assert check == True
