#CYB130T - Week 1
# Lab 1.32
'''
1.32 LAB: Using math functions
Given three floating-point numbers x, y, and z, output x to the power of z, x to the power of (y to the power of z), the absolute value of (x minus y), and the square root of (x to the power of z).

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3, your_value4))

Ex: If the input is:

5.0
1.5
3.2
Then the output is:

172.47 361.66 3.50 13.13
'''

import math

x = float(input())
y = float(input())
z = float(input())

your_value1 = pow(x, z)
your_value2 = pow(x, pow(y, z))
your_value3 = abs(x - y)
your_value4 = math.sqrt(pow(x, z))


print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3, your_value4))
