#CYB130T - Week 5
# Lab 5.6
'''
5.6 LAB: Name format
Many documents use a specific format for a person's name. Write a program whose input is:

firstName middleName lastName

and whose output is:

lastName, firstInitial.middleInitial.

Ex: If the input is:

Pat Silly Doe
the output is:

Doe, P.S.
If the input has the form:

firstName lastName

the output is:

lastName, firstInitial.

Ex: If the input is:

Julia Clark
the output is:

Clark, J.
'''

full_name = input()
mod_name = full_name.split(' ')
temp = '.'.join([mod_name[i][0] for i in range (0, len(mod_name) - 1)])
if temp == '':
    print (mod_name[-1])
else:
    print (mod_name[-1] + ', ' + temp + '.')
