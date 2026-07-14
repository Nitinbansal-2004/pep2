# Using list comprehension, create a list of all numbers from 1 to 50 that are divisible by 3.
# Print the list and also print its length. [5 marks] 
n = []
for x in range(1, 51):
    if x % 3 == 0:
        n.append(x)
print(n)
print(len(n))

