from flask import request
from src.drivers.jwt_handler import JwtHandler

def jwt_auth_verification():
    jwt_handler = JwtHandler()
    bearer_token = request.headers("Authorization")
    user_id = request.headers("user_id")

    if not bearer_token or not user_id:
        raise Exception("Invalid authentication input")
    
    token = bearer_token.split()[1]
    token_info = jwt_handler.decode_jwt_token(token)
    token_uid = token_info["user_id"]

    if token_uid and (int(user_id) == int(token_uid)):
        return token_info
    
    raise Exception("User unauthorized")
