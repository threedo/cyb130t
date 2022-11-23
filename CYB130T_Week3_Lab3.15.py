#CYB130T - Week 3
# Lab 3.15
'''
3.15 LAB: Password modifier
Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "!" to the end of the input string.

i becomes 1
a becomes @
m becomes M
B becomes 8
s becomes $
Ex: If the input is:

mypassword
the output is:

Myp@$$word!
Hint: Python strings are immutable, but support string concatenation. Store and build the stronger password in the given password variable.
'''
word = input()
password = ''

word = word.replace('i','1').replace('a','@').replace('m','M').replace('B','8').replace('s','$')
print(word+'!')
