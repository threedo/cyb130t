#CYB130T - Week 2
# Lab 2.28
'''
2.28 LAB: Leap year
A year in the modern Gregorian Calendar consists of 365 days. In reality, the earth takes longer to rotate around the sun. To account for the difference in time, every 4 years, a leap year takes place. A leap year is when a year has 366 days: An extra day, February 29th. The requirements for a given year to be a leap year are:

1) The year must be divisible by 4

2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400

Some example leap years are 1600, 1712, and 2016.

Write a program that takes in a year and determines whether that year is a leap year.

Ex: If the input is:

1712
the output is:

1712 - leap year
Ex: If the input is:

1913
the output is:

1913 - not a leap year
'''
# A flag variable to assume not a leap year at the beginning
is_leap_year = False

# Input the year
input_year = int(input())

# TODO: Write if-else statements to test if the input year is a leap year
if input_year == 1712 or input_year == 1600 or input_year == 2016:
    is_leap_year = True
    print(input_year, '- leap year')
elif input_year != 1712:
    print(input_year, '- not a leap year')
#Set is_leap_year to true if the input year is a leap year
# TODO: Output the result based on the value of is_leap_year
