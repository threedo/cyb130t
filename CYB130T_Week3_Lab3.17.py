#CYB130T - Week 3
# Lab 3.17
'''
3.17 LAB: Print string in reverse
Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

Ex: If the input is:

Hello there
Hey
done
then the output is:

ereht olleH
yeH
'''

while True:
    string = str(input())
    if string == "Done" or string == "done" or string == "d":
        break
    else:
        print(string[::-1])
