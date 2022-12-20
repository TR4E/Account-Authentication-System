from src.main.account import AccountManager


def execute():
    email = input("Enter your Email: ")

    account = AccountManager.getAccount(email)
    if account is None:
        print("Failed to Change Password: Invalid Email")
        return

    password = input("Enter your Password: ")

    if not account.isPassword(password):
        print("Failed to Change Password: Incorrect Password")
        return

    new_password = input("Enter a Password: ")

    account.setPassword(new_password)

    AccountManager.saveAccount(account)

    print("You have updated your password!")
