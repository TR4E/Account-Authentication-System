from src.main.account import AccountManager


def execute(args):
    emails = []

    for account in AccountManager.ACCOUNTS.values():
        emails.append(account.getEmail())

    print("Showing " + str(len(emails)) + " Accounts: [" + (", ".join(emails)) + "]")
