from src.main.account import AccountManager


class Account:

    def __init__(self, email, password, created):
        self.EMAIL = email
        self.PASSWORD = password
        self.CREATED = created

    def getEmail(self):
        return self.EMAIL

    def getPassword(self):
        return self.PASSWORD

    def setPassword(self, password):
        self.PASSWORD = AccountManager.createPassword(self.getEmail(), password)

    def isPassword(self, password):
        return self.getPassword() == AccountManager.createPassword(self.getEmail(), password)

    def getCreated(self):
        return self.CREATED
