'''
    counter.py
    Khalid Hussain, 17 September 2018
	Updated 17 September 2018
    Adapted from a program written by Jeff Ondich

    This program counts the number of lines in a file specified by the user.
    It also counts the number of lines that contain at least 80 characters.

    To test this program, create a text file (called, say, testdata.txt)
    with a bunch of lines, plus at least one line that's longer than
    80 characters.  Then run

       python3 counter.py
       File name, please: testdata.txt
       ...

    to see how many lines and how many long (>= 80) lines are in the file.
'''

input_file_name = input('File name, please: ')
input_file = open(input_file_name)

number_of_lines = 0
number_of_long_lines = 0
number_of_kinda_short_lines = 0
number_of_The_words = 0
number_of_the_words = 0
number_of_blank_spaces = 0

for line in input_file:
    number_of_lines = number_of_lines + 1
    if len(line) >= 80:
        number_of_long_lines = number_of_long_lines + 1
    if len(line) <= 80:
        number_of_kinda_short_lines = number_of_kinda_short_lines + 1
    if line[0: 3] == "The":
        number_of_The_words = number_of_The_words + 1
    if line[0: 3] == "the":
        number_of_the_words = number_of_the_words + 1
    if not line.split():
        number_of_blank_spaces = number_of_blank_spaces + 1
input_file.close()

print('The number of lines in', input_file_name, 'is', number_of_lines)
print('The number of long lines (80 chars or more) is', number_of_long_lines)
print('The number of lines (80 chars or less) is', number_of_kinda_short_lines)
print('The number of lines that start with the string "The" is', number_of_The_words)
print('The number of lines that start with the string "the" is', number_of_the_words)
print('The number of lines that are blank spaces is', number_of_blank_spaces)
