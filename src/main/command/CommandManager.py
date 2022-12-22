COMMANDS = {}


def addCommand(name, command):
    COMMANDS[name.lower()] = command


def getCommand(name):
    name = name.lower()

    if name in COMMANDS:
        return COMMANDS[name]
    return None


def getArgument(args, index, input_text):
    if args is None:
        return input(input_text)

    return args[index]
