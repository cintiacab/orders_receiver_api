import os

jwt_data = {
    "KEY" : os.getenv("KEY"),
    "ALGORITHM" : os.getenv("ALGORITHM"),
    "JWT_HOURS" : os.getenv("JWT_HOURS")
}
