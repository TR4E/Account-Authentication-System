from src.main.account.Account import Account
from src.main.account.commands import RegisterCommand, LoginCommand, ListCommand
from src.main.command import CommandManager
from src.main.utility import UtilCrypt, UtilJson

ACCOUNTS = {}


def addAccount(account):
    ACCOUNTS[account.getEmail().lower()] = account


def saveAccount(account):
    data = {
        account.getEmail(): {
            "Password": account.getPassword(),
            "Created": account.getCreated()
        }
    }

    UtilJson.saveJson("accounts", data)


def getAccount(email):
    email = email.lower()

    if email in ACCOUNTS:
        return ACCOUNTS[email]
    return None


def createPassword(email, password):
    return UtilCrypt.encrypt(email + ":" + password)


def loadAccounts():
    for (key, value) in UtilJson.getJson("accounts").items():
        account = Account(key, value["Password"], value["Created"])

        addAccount(account)


def registerCommands():
    CommandManager.addCommand("list", ListCommand)
    CommandManager.addCommand("register", RegisterCommand)
    CommandManager.addCommand("login", LoginCommand)
