#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number
if number < 0:
	last_digit = number * -1
last_digit = last_digit % 10
if last_digit > 5:
	str = "and is greater than 5"
if last_digit < 6:
	if last_digit == 0:
		str = "and is 0"
	else:
		str = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} {str}")
