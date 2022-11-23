#CYB130T - Week 2
# Lab 2.12

'''
2.12 LAB: Phone number breakdown
Given an integer representing a 10-digit phone number, follow the TODO comments to complete that program that outputs the area code, prefix, and line number using the format (800) 555-1212.

Ex: If the input is:

8005551212
the output is:

(800) 555-1212
Hint: Use % to get the desired rightmost digits. Ex: The rightmost 2 digits of 572 is gotten by 572 % 100, which is 72.

Hint: Use // to shift right by the desired amount. Ex: Shifting 572 right by 2 digits is done by 572 // 100, which yields 5. (Recall integer division discards the fraction).

For simplicity, assume any part starts with a non-zero digit. So 0119998888 is not allowed.
'''

phone_number = int(input())
line_number = phone_number % 10000
phone_number = phone_number // 10000
prefix_number = phone_number % 1000
phone_number = phone_number // 1000
area_code_number = phone_number
print('({0}) {1}-{2}'.format(area_code_number, prefix_number, line_number))
