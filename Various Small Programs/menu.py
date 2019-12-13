"""
menu.py

String Menu: Created by Khalid Hussain

CS 111.01, Professor Jeffrey Ondich, 30 September 2018

"""

user_string = input("What is your string (in lowercase letters)?: ")     # Ask the user for a string

def print_menu():      # Next print menu options, formatted from http://cs.carleton.edu/faculty/jondich/courses/cs111_f18/assignments/10_menu.html
    print()
    print('A. How many characters are in the string?')
    print('B. How many letters are in the string?')
    print('C. How many consonants are in the string?')
    print('D. Is the string a palindrome?')
    print('E. What is the Caesar Cipher (shift 3) of the string?')
    print('Q. Quit')
    print()


def characters_in_string(): # Operations for response to 'A'
    length = print(len(user_string))
    return length

def letters_in_string():  # Operations for response to 'B'
    user_string_characters = user_string.replace(" ", "")
    amount_of_letters = print(len(user_string_characters))
    return amount_of_letters

def consonants_in_string():  # Operations for response to 'C'
    consonants = list("bcdfghjklmnpqrstvwxyz")
    consonants_total = sum(user_string.count(c) for c in consonants)
    number_of_consonants = print(consonants_total)
    return number_of_consonants

def palindrome(str):        # Operations for response to 'D'
    for i in range(0, len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

def cipher(string):         # Operations for response to 'E', converting string to ASCII
    shift = 3
    for ch in string:
        if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
            encrypted_message = [ ord(ch) + shift for ch in string ]
        if ch == 'z':
            encrypted_message = [ ord('`') + shift for ch in string ]
        if ch == 'Z':
            encrypted_message = [ ord('@') + shift for ch in string ]
    return (encrypted_message)

def cipher_decrypt(numbers): # Operations for response to 'E', converting ASCII to ciphered string
    decrypted_message = ""
    for ch in numbers:
        if (ch >= 97 and ch <= 122) or (ch >= 65 and ch <= 90):
            decrypted_message += chr(ch)
    return(decrypted_message)

def quit():                 # Operations for response to 'Q'
    exit()


def do_operation(selection):  # Calling of the functions responsible for each answer choice
    if selection == 'A':
        characters_in_string()
    elif selection == 'B':
        letters_in_string()
    elif selection == 'C':
        consonants_in_string()
    elif selection == 'D':
        ans = palindrome(user_string)
        if (ans):
            print("Yes")
        else:
            print("No")
    elif selection == 'E':
        typed = cipher(user_string)
        typed2 = cipher_decrypt(typed)
        print("Your cipher text (with shift 3) is: ", typed2)
    elif selection == 'Q':
        print("Okay, goodbye!")
        quit()


while True:                     # The main program responsible for printing menu, and looping it once receiving answer
    print_menu()
    response = input('Your choice? ')
    do_operation(response)
