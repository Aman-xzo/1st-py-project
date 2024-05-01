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
    user = input("Enter word for encrypting :").lower()
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
    

while True:
    user_want_to_do = input("Enter 'E' for encrypting and 'D' for decrypting or 'X' for stop program :").lower()

    if user_want_to_do == "e":
        encrypytion()

    elif user_want_to_do == "d":
        decryption()

    elif user_want_to_do == "x":
        break
    else:
        break

print("Program end")