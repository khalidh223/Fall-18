# caesar.py
# Caesar Cipher: Created by Khalid Hussain
# CS 111.01, Professor Jeffrey Ondich, 09/24/18

plain_text_a2q = input("What is your plaintext?: ")
def caesar_encrypt(plaintext):
    shift_a2q = int(input("What shift do you want to use?: "))
    for ch in plaintext:
        if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
            encrypted_message = [ ord(ch) + shift_a2q for ch in plaintext ]
        if ch == 'z':
            encrypted_message = [ ord('`') + shift_a2q for ch in plaintext ]
        if ch == 'Z':
            encrypted_message = [ ord('@') + shift_a2q for ch in plaintext ]
    return(encrypted_message)
def caesar_decrypt(numericaltext):
    decrypted_message = ""
    for ch in numericaltext:
        if (ch >= 97 and ch <= 122) or (ch >= 65 and ch <= 90):
            decrypted_message += chr(ch)
    return(decrypted_message)

typed = caesar_encrypt(plain_text_a2q)

typed2 = caesar_decrypt(typed)
print("Your cipher text is: ", typed2)
print("Your plain text was: ", plain_text_a2q)
