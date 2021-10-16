#!bin/bash/python3
#Playful Cipher

def playful_enc():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext = ""
    enc_key = ""
    enc_string = ""

    #Enter a message you wish to encypt
    plaintext = input("Plaintext Message: ")
    plaintext = plaintext.lower()

    #Length of the plain text
    ptxt_length = len(plaintext)

    #Enter an ecryption key
    enc_key = input("Encryption Key: ")
    plaintext = plaintext.lower()

    #Expands the key to make it longer than the plaintext
    expanded_key = enc_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < ptxt_length:
    # Adds another repetition of the encryption key
        expanded_key = expanded_key + enc_key
        expanded_key_length = len(expanded_key)
        
        key_position = 0 

    for letter in plaintext:
        if letter in alphabet:
            position = alphabet.find(letter)
        # moves along key and finds the characters value
        key_character = expanded_key[key_position]
        key_character_position = alphabet.find(key_character)
        key_position = key_position + 1
        # changes the original of the input string character
        new_position = position + key_character_position
        if new_position > 26:
            new_position = new_position - 26
        new_character = alphabet[new_position]
        enc_string = enc_string + new_character
    else:
        enc_string = enc_string + letter
        return(enc_string)

#Reverse cipher
reverse = playful_enc()[::-1]

#Reverse cipher into sha3_512 hash
import hashlib

result = hashlib.sha3_512(reverse.encode())

print (result.hexdigest())
