from string import ascii_lowercase
from itertools import cycle

def cipher(key, message):
    key = cycle([ascii_lowercase.index(letter) for letter in key])
    message = [ascii_lowercase.index(letter) for letter in message]
    ciphered_message= "".join([ascii_lowercase[(next(key) + letter) % 26] for letter in message])
    return ciphered_message

def decipher(key,message):
    key = cycle([ascii_lowercase.index(letter) for letter in key])
    message = [ascii_lowercase.index(letter) for letter in message]
    deciphered_message = "".join([ascii_lowercase[(letter - next(key)) % 26] for letter in message])
    return deciphered_message