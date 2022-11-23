#CYB130T - Week 4
# Lab 4.21
'''
4.21 LAB: Leap year - functions
A year in the modern Gregorian Calendar consists of 365 days. In reality, the earth takes longer to rotate around the sun. To account for the difference in time, every 4 years, a leap year takes place. A leap year is when a year has 366 days: An extra day, February 29th. The requirements for a given year to be a leap year are:

1) The year must be divisible by 4

2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400

Some example leap years are 1600, 1712, and 2016.

Write a program that takes in a year and determines whether that year is a leap year.

Ex: If the input is:

1712
the output is:

1712 is a leap year.
Ex: If the input is:

1913
the output is:

1913 is not a leap year.
Your program must define and call the following function. The function should return True if the input year is a leap year or False otherwise.
def is_leap_year(user_year)
'''

def is_leap_year(user_year):
    if(user_year % 400 == 0):
        return True
    elif user_year % 100 == 0:
        return False
    elif user_year%4 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    user_year = int(input())
    if is_leap_year(user_year):
        print(user_year, "is a leap year.")
    else:
        print(user_year, "is not a leap year.")
