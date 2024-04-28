dict1 = {
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
        'z': '/',
        ' ': ' '
    }

dict2 = {value:key for key,value in dict1.items()}

def encrypytion():
    user = input("Enter word for encrypting :")
    encrypyted = ""
    for i in user:
        encrypyted += dict1[i]
    print(encrypyted)

def decryption():
    user1 = input("Enter word for decrypting :")
    decrypted = ""
    for i in user1:
        decrypted += dict2[i]
    print(decrypted)
    

encrypytion()
decryption()

