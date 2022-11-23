#CYB130T - Week 2
# Lab 2.27
'''
2.27 LAB: Exact change
Write a program with total change amount (in cents) as an integer input, and output the change using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

Hint: Start from the largest denomination. Divide the change amount by the number of cents in the denomination to get the number of coins used. The remainder of the division is used to find the number of coins used in the next denomination. Ex: value // 100 gives the number of dollars used. The remainder is divided by 25 to find the number of quarters used.

Ex: If the input is:

0
(or less than 0), the output is:

No change
Ex: If the input is:

45
the output is:

1 Quarter
2 Dimes
'''
def main():
  input_val = int(input())
  if input_val <= 0:
    print('No change')
  else:
    num_dollars = input_val // 100
    input_val %= 100
    num_quarters = input_val // 25
    input_val %= 25
    num_dimes = input_val // 10
    input_val %= 10
    num_nickels = input_val // 5
    input_val %= 5
    num_pennies = input_val

    if num_dollars >1:
        print('%d Dollars' % num_dollars)
    elif num_dollars ==1:
        print('%d Dollar' % num_dollars)
    if num_quarters > 1:
        print('%d Quarters' % num_quarters)
    elif num_quarters ==1:
        print('%d Quarter' % num_quarters)
    if num_dimes >1:
        print('%d Dimes' % num_dimes)
    elif num_dimes ==1:
        print('%d Dime' % num_dimes)
    if num_nickels >1:
        print('%d Nickels' % num_nickels)
    elif num_nickels ==1:
        print('%d Nickel' % num_nickels)
    if num_pennies >1:
        print('%d Pennies' % num_pennies)
    elif num_pennies ==1:
        print('%d Penny' % num_pennies)
main()
