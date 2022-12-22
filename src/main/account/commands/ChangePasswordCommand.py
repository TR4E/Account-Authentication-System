from src.main.account import AccountManager
from src.main.command import CommandManager


def execute(args):
    email = CommandManager.getArgument(args, 0, "Enter a Email: ")

    account = AccountManager.getAccount(email)
    if account is None:
        print("Failed to Change Password: Invalid Email")
        return

    password = CommandManager.getArgument(args, 1, "Enter a Password: ")

    if not account.isPassword(password):
        print("Failed to Change Password: Incorrect Password")
        return

    new_password = CommandManager.getArgument(args, 2, "Enter a Password: ")

    account.setPassword(new_password)

    AccountManager.saveAccount(account)

    print("You have updated your password!")
