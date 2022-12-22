from src.main.account import AccountManager
from src.main.command import CommandManager

if __name__ == "__main__":
    AccountManager.registerCommands()
    AccountManager.loadAccounts()

    while True:
        command_name = input("> ")
        args = None

        if " " in command_name:
            tokens = list(command_name.split(" "))

            command_name = tokens.pop(0)
            args = tokens

        command = CommandManager.getCommand(command_name)
        if command is None:
            print("Invalid Command!")
            continue

        command.execute(args)
