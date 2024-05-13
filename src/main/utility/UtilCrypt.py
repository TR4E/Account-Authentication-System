import hashlib

PEPPER = "A5kv$xoY56!saDg_"

def encrypt(string):
    text = string

    for i in range(32):
        text = hashlib.sha512(bytes("{}{}".format(text, PEPPER), "UTF-8")).hexdigest()

    text = extraEncrypt(text)

    return text


def extraEncrypt(string):
    replaces = [
        "@", "$", "%", "^", "&", "_", "-", "+", "*", "!"
    ]

    result = ""

    for (index, character) in enumerate(string):
        new_result = character

        if character.isnumeric() and index % 4 == 0:
            new_result = replaces[int(character)]

        result += new_result

    return result
