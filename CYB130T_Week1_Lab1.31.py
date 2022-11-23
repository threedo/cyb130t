#CYB130T - Week 1
# Lab 1.31
'''
1.31 LAB: Expression for calories burned during workout
The following equations estimate the calories burned when exercising (source):

Women: Calories = ( (Age x 0.074) — (Weight x 0.05741) + (Heart Rate x 0.4472) — 20.4022 ) x Time / 4.184

Men: Calories = ( (Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) — 55.0969 ) x Time / 4.184

Write a program using inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes), respectively. Output calories burned for women and men.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('Men: {:.2f} calories'.format(calories_man))

Ex: If the input is:

49
155
148
60
Then the output is:

Women: 580.94 calories
Men: 891.47 calories
'''

''' Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184 '''
''' Men: Calories = ((Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184 '''

age_years = int(input())
weight_pounds = int(input())
heart_rate_bpm = int(input())
time_minutes = int(input())


calories_man = ((age_years * 0.2017) + (weight_pounds * 0.09036) + (heart_rate_bpm * 0.6309) - 55.0969) * time_minutes / 4.184
calories_women = ((age_years * 0.074) - (weight_pounds * 0.05741) + (heart_rate_bpm * 0.4472) - 20.4022) * time_minutes / 4.184

print('Women: {:.2f} calories'.format(calories_women))
print('Men: {:.2f} calories'.format(calories_man))
