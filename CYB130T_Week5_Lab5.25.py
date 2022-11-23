#CYB130T - Week 5
# Lab 5.25
'''
5.25 LAB: Elements in a range
Write a program that first gets a list of integers from input. That list is followed by two more integers representing lower and upper bounds of a range. Your program should output all integers from the list that are within that range (inclusive of the bounds).

Ex: If the input is:

25 51 0 200 33
0 50
the output is:

25 0 33
The bounds are 0-50, so 51 and 200 are out of range and thus not output.

For coding simplicity, follow each output integer by a space, even the last one. Do not end with newline.
'''

input_numbers = [int(x) for x in input().split(' ')]
input_range = [int(x) for x in input().split(' ')]

for number in input_numbers:
    if input_range[0] <= number <= input_range[1]:
        print('{}'.format(number), end = ' ')
