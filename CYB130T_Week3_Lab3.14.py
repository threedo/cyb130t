#CYB130T - Week 3
# Lab 3.14
'''
3.14 LAB: Count input length without spaces, periods, exclamation points, or commas
Instructor note:
Note: this section of your textbook contains activities that you will complete for points. To ensure your work is scored, please access this page from the assignment link provided in Blackboard. If you did not access this page via Blackboard, please do so now.

Given a line of text as input, output the number of characters excluding spaces, periods, exclamation points, or commas.

Ex: If the input is:

Listen, Mr. Jones, calm down.
the output is:

21
Note: Account for all characters that aren't spaces, periods, exclamation points, or commas (Ex: "r", "2", "?").
'''
user_text = input()

numOfChars = 0
count = 0
for i in user_text:
    if user_text[count] != ' ' and user_text[count] != '.' and user_text[count] != ',' and user_text[count] != '!':
        numOfChars += 1
    count += 1
print(numOfChars)
