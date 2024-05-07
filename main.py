dict1 = {
        'a': '@^&@',
        'b': '!*(@',
        'c': '#GUW',
        'd': '$IUH',
        'e': '%H&@',
        'f': '^%@B',
        'g': '&JW*',
        'h': '*@S9',
        'i': '(<sW',
        'j': ')}W|',
        'k': '_V~^',
        'l': '-hsN',
        'm': '+@$%',
        'n': '=V(#',
        'o': '[B$@',
        'p': ']G#Y',
        'q': '{C@(',
        'r': '}BW%',
        's': ':BA%',
        't': ';N$@',
        'u': '<HW)',
        'v': '$@->',
        'w': ',CZZ',
        'x': '.HW@',
        'y': '?jw5',
        'z': '/scF',
        ' ': '?^s8'
    }

dict2 = {value:key for key,value in dict1.items()}

# Function for Encrypting words

def encrypytion():
    user = input("\n =>Enter word for encrypting :").lower()
    encrypyted_word = ""
    for i in user:
        if i in dict1:
            encrypyted_word += dict1[i]
        else:
            encrypyted_word += i
    
    encrypyted_word_v2 = encrypyted_word[::-1] 

    print(f"\n =>{encrypyted_word_v2}")

# function for Decrypting (encrypted words)

def decryption():
    l1 = []
    val1 = 0
    val2 = 4
    decrypted_word = "" 

    user1 = input("\n =>Enter word for decrypting :")[::-1]

    while True:
        l1.append(user1[val1:val2])
        val1 = val2
        val2 += 4

        if val2 >= len(user1)+1:
            break
        
    for i in l1:
        if i in dict2:
            decrypted_word += dict2[i]
        else:
            decrypted_word += i

    print(decrypted_word.capitalize())

# what user want to do 

while True:
    user_want_to_do = input("\n =>Enter 'E' for encrypting and 'D' for decrypting or 'X' for stop program :").lower()

    if user_want_to_do == "e":
        encrypytion()

    elif user_want_to_do == "d":
        decryption()

    elif user_want_to_do == "x":
        break
    else:
        break

print("Program end")
