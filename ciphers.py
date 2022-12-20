def encryptAtbashCipher(text):
    reversedString = ''
    for letter in text:
        reversedString += chr(219 - ord(letter))
    return reversedString


def decryptAtbashCipher(text):
    return encryptAtbashCipher(text)


def encryptCaesarCipher(text, key):
    key %= 26
    shiftedText = ""
    mappingDictionary = {'.': ',',
                         ',': '.',
                         '!': '?',
                         '?': '!',
                         '0': '1',
                         '1': '0',
                         '2': '3',
                         '3': '2',
                         '4': '5',
                         '5': '4',
                         '6': '7',
                         '7': '6',
                         '8': '9',
                         '9': '8'}
    for letter in text:
        if letter.isupper():
            shiftedText += chr((ord(letter) + key - 65) % 26 + 65)
        elif letter.islower():
            shiftedText += chr((ord(letter) + key - 97) % 26 + 97)
        elif letter in mappingDictionary.values():
            shiftedText += mappingDictionary.get(letter)
        else:
            shiftedText += letter
    return shiftedText


def decryptCaesarCipher(text, key):
    return encryptCaesarCipher(text, -key)


def encryptVigenereCipher(text, keyList):
    encryptedText = ""
    for index in range(len(text)):
        encryptedText += encryptCaesarCipher(text[index], keyList[index % len(keyList)])
    return encryptedText


def decryptVigenereCipher(text, keyList):
    keyList = [-number for number in keyList]
    return encryptVigenereCipher(text, keyList)


def encryptSimpleEnigmaCipher(text, keys):
    def enigmaHelper(char, keys):
        for key in keys:
            if char.isupper():
                char = (key[ord(char) - 65]).upper()
            elif char.islower():
                char = key[ord(char) - 97]
        return char
    enigmedText = ""
    for letter in text:
        enigmedText += enigmaHelper(letter, keys)
    return enigmedText



def decryptSimpleEnigmaCipher(text, keys):
    pass



# # Uncomment for testing.
# key1 = "bcdefghijklmnopqrstuvwxyza"
# key2 = "qwertyuioplkjhgfdsazxcvbnm"
# key3 = "zxcvbnmlkjhgfdsaqwertyuiop"
# # Encryption tests
# print(encryptAtbashCipher("programming")) # kiltiznnrmt
# print(encryptCaesarCipher("Cipher programming 101!",2)) # Ekrjgt rtqitcookpi 010?
# print(encryptVigenereCipher("Cipher programming 101!", [1, 3, 2]))  # Dlriht stpjtbpojqi 010?
# print(encryptSimpleEnigmaCipher("Cipher programming 101!", (key1, key2, key3)))  # Wavsoz vznkzullamk 101!
# # Decryption tests
# print(decryptAtbashCipher(encryptAtbashCipher("programming")))
# print(decryptCaesarCipher(encryptCaesarCipher("Cipher programming 101!",2),2))
# print(decryptVigenereCipher(encryptVigenereCipher("Cipher programming 101!",[1,3,2]),[1,3,2]))
# print(decryptSimpleEnigmaCipher(encryptSimpleEnigmaCipher("Cipher programming 101!",(key1,key2,key3)),(key1,key2,key3)))
# # Comment out before submitting.
