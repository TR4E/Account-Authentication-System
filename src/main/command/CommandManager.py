COMMANDS = {}


def addCommand(name, command):
    COMMANDS[name.lower()] = command


def getCommand(name):
    name = name.lower()

    if name in COMMANDS:
        return COMMANDS[name]
    return None


def getCommandInfo(text):
    command_name = text
    args = []

    if " " in command_name:
        tokens = list(command_name.split(" "))

        command_name = tokens.pop(0)
        args = tokens

    return command_name, args


def getArgument(args, index, input_text):
    if args is not None and len(args) > 0 and args[index] is not None:
        return args[index]

    return input(input_text)
