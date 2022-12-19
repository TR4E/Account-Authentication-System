import sys

ROOT_PATH = "" if "linux" in sys.platform else (sys.path[1] + "\\")


def getLines(file_name):
    lines = []

    with open(ROOT_PATH + "src\\resources\\" + file_name, "r") as file:
        for line in file:
            lines.append(line.strip())

    return lines


def writeToFile(file_name, line):
    FILE_PATH = ROOT_PATH + "src\\resources\\" + file_name + ".txt"

    if line in getLines(file_name):
        return

    with open(FILE_PATH, "a") as file:
        file.write(line + "\n")
