#CYB130T - Week 4
# Lab 4.18
'''
4.18 LAB: Miles to track laps
Instructor note:
Note: this section of your textbook contains activities that you will complete for points. To ensure your work is scored, please access this page from the assignment link provided in Blackboard. If you did not access this page via Blackboard, please do so now.

One lap around a standard high-school running track is exactly 0.25 miles. Write the function miles_to_laps() that takes a number of miles as an argument and returns the number of laps. Complete the program to output the number of laps.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('{:.2f}'.format(your_value))

Ex: If the input is:

1.5
the output is:

6.00
Ex: If the input is:

2.2
the output is:

8.80
Your program must define and call the following function:
def miles_to_laps(user_miles)
'''

def miles_to_laps(user_miles):
    return user_miles/0.25

if __name__ == '__main__':
    miles=float(input())
    laps=miles_to_laps(miles)
    print('{:.2f}'.format(laps))
