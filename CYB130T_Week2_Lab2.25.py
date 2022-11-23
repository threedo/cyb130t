#CYB130T - Week 2
# Lab 2.25

'''
2.25 LAB: Smallest number
Write a program whose inputs are three integers, and whose output is the smallest of the three values.

Ex: If the input is:

7
15
3
the output is:

3
'''
# TODO: Input three integers
a = int(input())
b = int(input())
c = int(input())

# TODO: Use if-else statements to determine which of the three integers is the smallest
# Hint: Compare each integer against the others
if a <= b and a <= c:
    print(a)
elif (b <= a) and (b <= c):
    print(b)
elif (c <= a) and (c <= b):
    print(c)
