from src.main.account.Account import Account
from src.main.account.commands import RegisterCommand, LoginCommand, ListCommand, ChangePasswordCommand, DeleteCommand
from src.main.command import CommandManager
from src.main.utility import UtilCrypt, UtilJson

ACCOUNTS = {}


def addAccount(account):
    ACCOUNTS[account.getEmail().lower()] = account


def removeAccount(account):
    ACCOUNTS.pop(account.getEmail().lower())


def saveAccount(account):
    data = {
        account.getEmail(): {
            "Password": account.getPassword(),
            "Created": account.getCreated()
        }
    }

    UtilJson.saveJson("accounts.json", data)


def deleteAccount(account):
    data = UtilJson.getJson("accounts.json")

    data.pop(account.getEmail())

    UtilJson.saveJson("accounts.json", data, overwrite=True)


def getAccount(email):
    email = email.lower()

    if email in ACCOUNTS:
        return ACCOUNTS[email]
    return None


def createPassword(email, password):
    return UtilCrypt.encrypt(email + ":" + password)


def loadAccounts():
    for (key, value) in UtilJson.getJson("accounts.json").items():
        account = Account(key, value["Password"], value["Created"])

        addAccount(account)


def registerCommands():
    CommandManager.addCommand("changepassword", ChangePasswordCommand)
    CommandManager.addCommand("delete", DeleteCommand)
    CommandManager.addCommand("list", ListCommand)
    CommandManager.addCommand("register", RegisterCommand)
    CommandManager.addCommand("login", LoginCommand)
