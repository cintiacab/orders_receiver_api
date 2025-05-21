class HttpNotFound(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.name = "NotFound"
        self.status_code = 404
        self.message = message
