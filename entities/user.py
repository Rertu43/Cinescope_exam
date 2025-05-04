from api.api_manager import APIManager

class User:
    def __init__(self, email: str, password: str, roles: list, api: APIManager):
        self.email = email
        self.password = password
        self.roles = roles
        self.api = api # для передачи объекта API manager

    @property
    def creds(self):
        """Возвращает (email, password)"""
        return self.email, self.password