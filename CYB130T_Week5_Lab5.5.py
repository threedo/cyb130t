#CYB130T - Week 5
# Lab 5.5
'''
5.5 LAB: Checker for integer string
Instructor note:
Note: this section of your textbook contains activities that you will complete for points. To ensure your work is scored, please access this page from the assignment link provided in Blackboard. If you did not access this page via Blackboard, please do so now.

Forms often allow a user to enter an integer. Write a program that takes in a string representing an integer as input, and outputs yes if every character is a digit 0-9.

Ex: If the input is:

1995
the output is:

yes
Ex: If the input is:

42,000
or any string with a non-integer character, the output is:

no
'''

user_string = input()

isInt = True
for x in user_string:
    if not(x.isdigit()):
        isInt = False
        break
if isInt:
    print("yes")
else:
    print("no")
