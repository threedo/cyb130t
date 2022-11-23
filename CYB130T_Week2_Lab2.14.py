#CYB130T - Week 2
# Lab 2.14

'''
2.14 LAB: Simple statistics
Given 4 floating-point numbers. Use a string formatting expression with conversion specifiers to output their product and their average as integers (rounded), then as floating-point numbers.

Output each rounded integer using the following:
print('{:.0f}'.format(your_value))

Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
print('{:.3f}'.format(your_value))

Ex: If the input is:

8.3
10.4
5.0
4.8
the output is:

2072 7
2071.680 7.125
'''

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num_product = (num1) * (num2) * (num3) * (num4)
average_product = (num1) + (num2) + (num3) + (num4)
average_product = average_product / 4
print('{:.0f} {:.0f}'.format(num_product, average_product))
print('{:.3f} {:.3f}'.format(num_product, average_product))
