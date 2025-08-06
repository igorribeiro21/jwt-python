class HttpUnauthorizedError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.name = "Unathorized"
        self.status_code = 401