from flask import request
from src.drivers.jwt_handler import JwtHandler
from src.errors.errors_types.http_unauthorized_error import HttpUnauthorized

def jwt_auth_verification():
    jwt_handler = JwtHandler()
    bearer_token = request.headers.get("Authorization")
    user_id = request.headers.get("uid")

    if not bearer_token or not user_id:
        raise HttpUnauthorized("Invalid authentication information")
    
    token = bearer_token.split()[1]
    token_info = jwt_handler.decode_jwt_token(token)
    token_uid = token_info["user_id"]

    if token_uid and (int(user_id) == int(token_uid)):
        return token_info
    
    raise HttpUnauthorized("User unauthorized")
