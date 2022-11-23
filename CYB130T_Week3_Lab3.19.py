#CYB130T - Week 3
# Lab 3.19
'''
3.19 LAB: Output values in a list below a user defined amount
Write a program that first gets a list of integers from input. The input begins with an integer indicating the number of integers that follow. Then, get the last value from the input, which indicates a threshold. Output all integers less than or equal to that last threshold value.

Ex: If the input is:

5
50
60
140
200
75
100
the output is:

50,60,75,
The 5 indicates that there are five integers in the list, namely 50, 60, 140, 200, and 75. The 100 indicates that the program should output all integers less than or equal to 100, so the program outputs 50, 60, and 75.

For coding simplicity, follow every output value by a comma, including the last one.

Such functionality is common on sites like Amazon, where a user can filter results.
'''

import array
usr_in = input()

if not usr_in.isnumeric():
    print(usr_in, end=",")


number_of_new_inputs = int(usr_in)

array_of_inputs = array.array('i')


for i in range(number_of_new_inputs):
    usr_in = input()
    if not usr_in.isnumeric():
        print(usr_in, end=",")


    array_of_inputs.append(int(usr_in))

usr_in = input()
if not usr_in.isnumeric():
    print(usr_in, end=",")


max_val = int(usr_in)
for num in array_of_inputs:
    if num <= max_val:
        print(num, end=",")
