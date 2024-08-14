import math

total_salary=float(input())
"""
weekdays -80/hour
weekends -50/hour

weekends - n hours
weekdays - n+10 hours

total salary=80(n+10)+50(n)
total salary=80n+800+50n
total salary=130n+800
130n=total salary-800
n=(total salary -800)/130

"""
hours_worked=(total_salary-800)//130
weekend_hours=hours_worked
weekdays_hours=hours_worked+10
print(weekdays_hours)
print(weekend_hours)