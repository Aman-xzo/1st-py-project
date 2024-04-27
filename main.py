list = {
        'a': '@',
        'b': '!',
        'c': '#',
        'd': '$',
        'e': '%',
        'f': '^',
        'g': '&',
        'h': '*',
        'i': '(',
        'j': ')',
        'k': '_',
        'l': '-',
        'm': '+',
        'n': '=',
        'o': '[',
        'p': ']',
        'q': '{',
        'r': '}',
        's': ':',
        't': ';',
        'u': '<',
        'v': '>',
        'w': ',',
        'x': '.',
        'y': '?',
        'z': '/'
    }

def encrypytion():
    user = input("Enter word for encrypting :")
    encrypyted = ""
    for i in user:
        encrypyted += list[i]
    print(encrypyted)

encrypytion()