import jwt
from datetime import datetime, timedelta, timezone
from src.configuration.jwt_config import jwt_data

class JwtHandler:
    def create_jwt_token(self, body: dict) -> str:
        token = jwt.encode(
            payload={'exp': (
                datetime.now(timezone.utc) + 
                timedelta(hours=int(jwt_data["JWT_HOURS"]))
                ), **body
            },
            key= jwt_data["KEY"],
            algorithm= jwt_data["ALGORITHM"]
        )
        return token
    
    def decode_jwt_token(self, token: str) -> dict:
        token_information = jwt.decode(
            token,
            key= jwt_data["KEY"],
            algorithms= jwt_data["ALGORITHM"]
        )
        return token_information
