# Write a program that: a) Uses the map() function with a lambda to convert a list of temperatures 
# in Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32 b) Uses the filter() function with a lambda 
# to keep only temperatures above 100°F from the result c) Prints both results [10 marks] 

l=input('temperatures in celsius: ').split(',')
l1=list(map(lambda x: (float(x)*9/5)+32,l))
l2=list(filter(lambda x: x > 100, l1))
print("Temperatures in Fahrenheit:", l1)
print("Temperatures above 100°F:", l2)
