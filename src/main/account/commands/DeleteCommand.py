from src.main.account import AccountManager
from src.main.command import CommandManager


def execute(args):
    email = CommandManager.getArgument(args, 0, "Enter your Email: ")

    account = AccountManager.getAccount(email)
    if account is None:
        print("[-] Failed to Login: Invalid Email")
        return

    password = CommandManager.getArgument(args, 1, "Enter your Password: ")

    if not account.isPassword(password):
        print("[-] Failed to Login: Incorrect Password")
        return

    AccountManager.removeAccount(account)
    AccountManager.deleteAccount(account)

    print("[+] Successfully Deleted Account!")
