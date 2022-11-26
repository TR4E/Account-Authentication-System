import hashlib


def encrypt(string):
    text = string

    for i in range(32):
        text = hashlib.sha512(bytes(text, "UTF-8")).hexdigest()

    text = extraEncrypt(text)

    return text


def extraEncrypt(string):
    replaces = [
        "@", "$", "%", "^", "&", "_", "-", "+", "*", "!"
    ]

    result = ""

    for (index, character) in enumerate(string):
        new_result = character

        if character.isnumeric():
            if index % 4 == 0:
                new_result = replaces[int(character)]

        result += new_result

    return result
