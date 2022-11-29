from src.main.account import AccountManager


def execute():
    email = input("Enter your Email: ")

    account = AccountManager.getAccount(email)
    if account is None:
        print("Failed to Login: Invalid Email")
        return

    password = input("Enter your Password: ")

    if not account.isPassword(password):
        print("Failed to Login: Incorrect Password")
    else:
        print("Successfully Signed In!")
