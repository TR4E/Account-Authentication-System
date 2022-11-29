from src.main.account import AccountManager
from src.main.account.Account import Account
from src.main.utility import UtilTime


def execute():
    email = input("Enter a Email: ")

    if AccountManager.getAccount(email) is not None:
        print("Failed to Register: Email already exists")
        return

    password = input("Enter a Password: ")

    account = Account(email, AccountManager.createPassword(email, password), UtilTime.getSystemTime())

    AccountManager.addAccount(account)
    AccountManager.saveAccount(account)

    print("Successfully Registered Account!")
    print("Your Password: " + account.getPassword())
