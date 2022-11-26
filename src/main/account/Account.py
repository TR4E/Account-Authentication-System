from src.main.utility import UtilCrypt


class Account:

    def __init__(self, email, password, encrypt):
        self.EMAIL = email
        self.PASSWORD = UtilCrypt.encrypt(email + ":" + password) if encrypt else password

    def getEmail(self):
        return self.EMAIL

    def getPassword(self):
        return self.PASSWORD

    def setPassword(self, password):
        self.PASSWORD = password

    def isPassword(self, password):
        return self.PASSWORD == UtilCrypt.encrypt(self.getEmail() + ":" + password)
