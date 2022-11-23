#CYB130T - Week 4
# Lab 4.24
'''
4.24 LAB: Even/odd values in a list
Write a program that reads a list of integers, and outputs whether the list contains all even numbers, odd numbers, or neither. The input begins with an integer indicating the number of integers in the list. The first integer is not in the list.

Ex: If the input is:

5
2
4
6
8
10
the output is:

all even
Ex: If the input is:

5
1
-3
5
-7
9
the output is:

all odd
Ex: If the input is:

5
1
2
3
4
5
the output is:

not even or odd
Your program must define and call the following two functions. is_list_even() returns true if all integers in the list are even and false otherwise. is_list_odd() returns true if all integers in the list are odd and false otherwise.
def is_list_even(my_list)
def is_list_odd(my_list)
'''

def is_list_even(my_list):
        for i in range(len(my_list)):
            if my_list[i] % 2 != 0:
                return False
        return True

def is_list_odd(my_list):
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                return False
        return True

if __name__ == '__main__':
    my_list = []
    n = int(input())
    for i in range(n):
        my_list.append(int(input()))


    if is_list_even(my_list):
        print('all even')
    elif is_list_odd(my_list):
        print('all odd')
    else:
        print('not even or odd')
