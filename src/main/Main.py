from src.main.account import AccountManager
from src.main.command import CommandManager

if __name__ == "__main__":
    AccountManager.registerCommands()
    AccountManager.loadAccounts()

    while True:
        command_name = input("> ")

        command = CommandManager.getCommand(command_name)
        if command is None:
            print("Invalid Command!")
            continue

        command.execute()
