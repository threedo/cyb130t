#CYB130T - Week 2
# Lab 2.11

'''
2.11 LAB: Input and formatted output: Right-facing arrow
Given input characters for an arrow body and arrowhead, follow the TODO comments to complete the program that prints a right-facing arrow.

Ex: If the input is:

*
#
Then the output is:

      #
******##
******###
******##
      #
'''

# Input character for the arrow body
base_char = input()

# Input character for the arrowhead
head_char = input()

# Store first line of output in row1
row1 = '      ' + head_char
row2 = (base_char) + (base_char) + (base_char) + (base_char) + (base_char) + (base_char) + (head_char) + (head_char)
row3 = (base_char) + (base_char) + (base_char) + (base_char) + (base_char) + (base_char) + (head_char) + (head_char) + (head_char)

# TODO: Store second line of output in row2

# TODO: Store third line of output in row3


# Print rows
print(row1)
print(row2)
print(row3)
print(row2)
print(row1)
