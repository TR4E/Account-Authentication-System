import json
import os
import sys

ROOT_PATH = "" if "linux" in sys.platform else (sys.path[1] + "\\")


def getPath(file_name, file_ext):
    folder_path = ROOT_PATH + "src\\resources"

    if not os.path.exists(folder_path):
        os.system("mkdir " + folder_path)

    file_path = folder_path + "\\" + file_name + "." + file_ext

    if not os.path.exists(file_path):
        os.system("touch " + file_path)

    return file_path


def saveJson(file_name, new_data):
    data = dict(getJson(file_name).items())

    for (key, value) in new_data.items():
        data[key] = value

    path = getPath(file_name, "json")

    with open(path, "w") as file:
        file.write(json.dumps(data, indent=4))


def getJson(file_name):
    path = getPath(file_name, "json")

    try:
        with open(path, "r") as file:
            return json.load(file)
    except:
        return dict()
