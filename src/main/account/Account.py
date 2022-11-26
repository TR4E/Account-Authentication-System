from src.main.account import AccountManager


class Account:

    def __init__(self, email, password):
        self.EMAIL = email
        self.PASSWORD = password

    def getEmail(self):
        return self.EMAIL

    def getPassword(self):
        return self.PASSWORD

    def setPassword(self, password):
        self.PASSWORD = password

    def isPassword(self, password):
        return self.getPassword() == AccountManager.createPassword(self.getEmail(), password)
