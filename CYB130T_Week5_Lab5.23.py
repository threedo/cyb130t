#CYB130T - Week 5
# Lab 5.23
'''
5.23 LAB: Varied amount of input data
Instructor note:
Note: this section of your textbook contains activities that you will complete for points. To ensure your work is scored, please access this page from the assignment link provided in Blackboard. If you did not access this page via Blackboard, please do so now.

Statistics are often calculated with varying amounts of input data. Write a program that takes any number of integers as input, and outputs the average and max.

Ex: If the input is:

15 20 0 5
the output is:

10 20
Note: For output, round the average to the nearest integer.
'''


text = input()

numbers = text.split()

max=-1
sum=0

for n in numbers:

    sum+=int(n)

    if (int(n) > max):

        max = int(n)

avg = sum/len(numbers)

print(int(avg),max)
