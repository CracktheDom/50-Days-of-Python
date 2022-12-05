#!/usr/bin/env python3

"""Extra Challenge: Teacher's Salary
A school has asked you to write a program that will calculate
teachers' salaries. The program should ask the user to enter the
teacher's name, the number of periods taught in a month,
and the rate per period. The monthly salary is calculated by
multiplying the number of periods by the monthly rate.
The current monthly rate per period is $20. If a teacher has
more than 100 periods in a month, everything above 100 is
overtime. Overtime is $25 per period. For example, if a teacher
has taught 105 periods, their monthly gross salary should be
2,125. Write a function called your_salary that calculates a
teacher's gross salary. The function should return the
teacher's name, periods taught, and gross salary. Here is
how you should format your output:
Teacher: John Kelly,
Periods: 105
Gross salary:2,125"""

MONTHLY_RATE = 20
OVERTIME_RATE = 25

def your_salary():
	name = input("Teacher's name: ")
	periods_per_month = int(input("# of periods taught this month: "))
	overtime_pay = 0

	if periods_per_month > 100:
		overtime_pay = OVERTIME_RATE * (periods_per_month - 100)
		wages = MONTHLY_RATE * 100
	else:
		wages = MONTHLY_RATE * periods_per_month

	gross_wages = overtime_pay + wages

	return (f'Teacher: {name},\nPeriods: {periods_per_month}\nGross salary: {gross_wages:,.2f}')

print(your_salary())
