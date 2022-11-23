#CYB130T - Week 5
# Lab 5.7
'''
5.7 LAB: Palindrome
A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

Ex: If the input is:

bob
the output is:

bob is a palindrome
Ex: If the input is:

bobby
the output is:

bobby is not a palindrome
Hint: Start by removing spaces. Then check if a string is equivalent to it's reverse.
'''

string = input()
modified = ''.join(string.split(' '))

if(modified == modified[::-1]):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
