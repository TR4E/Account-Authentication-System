from src.main.account import AccountManager
from src.main.account.Account import Account


def register():
    email = input("Enter a Email: ")

    if AccountManager.getAccount(email) is not None:
        print("Failed to Register: Email already exists")
        return

    password = input("Enter a Password: ")

    account = Account(email, password, True)

    AccountManager.addAccount(account)
    AccountManager.saveAccount(account)

    print("Successfully Registered Account!")
    print("Your Password: " + account.getPassword())


def login():
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


if __name__ == "__main__":
    AccountManager.loadAccounts()

    while True:
        method = input("> ")

        if method == "register":
            register()
        elif method == "login":
            login()
        else:
            print("Available Commands: [register, login]")
