from src.main.account.Account import Account
from src.main.utility import UtilFile

ACCOUNTS = {}


def addAccount(account):
    ACCOUNTS[account.getEmail().lower()] = account


def saveAccount(account):
    UtilFile.writeToFile("accounts", account.getEmail() + ":" + account.getPassword())


def getAccount(email):
    if email in ACCOUNTS:
        return ACCOUNTS[email.lower()]
    return None


def loadAccounts():
    for account in UtilFile.getLines("accounts"):
        tokens = account.split(":")

        email = tokens[0]
        password = tokens[1]

        addAccount(Account(email, password, False))
    pass
