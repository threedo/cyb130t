#CYB130T - Week 1
# Lab 1.29
'''
1.29 LAB: Divide by x
Instructor note:
Note: this section of your textbook contains activities that you will complete for points. To ensure your work is scored, please access this page from the assignment link provided in Blackboard. If you did not access this page via Blackboard, please do so now.

Write a program using integers user_num and x as input, and output user_num divided by x three times.

Ex: If the input is:

2000
2
Then the output is:

1000 500 250
Note: In Python 3, integer division discards fractions. Ex: 6 // 4 is 1 (the 0.5 is discarded).
'''

user_num = int(input())
x = int(input())

print (user_num // x , user_num // x // x , user_num // x// x // x)
