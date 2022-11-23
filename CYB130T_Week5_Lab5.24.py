#CYB130T - Week 5
# Lab 5.24
'''
5.24 LAB: Filter and sort a list
Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).

Ex: If the input is:

10 -7 4 39 -6 12 2
the output is:

2 4 10 12 39
For coding simplicity, follow every output value by a space. Do not end with newline.
'''

s = input()
lst = [int(x) for x in s.split(" ") if int(x)>=0]
lst.sort()
for x in lst:
    print(x,end=" ")
