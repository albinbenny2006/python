import math 
import random
import datetime
import statistics
import os
print("squre root os 25 :",math.sqrt(25))
print("factorial of 5 :",math.factorial(5))
print("power 2,3:",math.pow(2,3))

print("random number(1-100):",random.randint(1,100))
print("random choice 'apple' 'banana' 'orange':",random.choice(["apple","banana","orange"]))

today=datetime.datetime.now()
print("current date and time:",today)
print("current year :",today.year)

numbers = [10, 20, 30, 40, 50]
print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("Standard deviation:", statistics.stdev(numbers))


print("Current directory:", os.getcwd())
