# Write a generator function fibonacci(n) that yields the first n Fibonacci numbers. 
# Use it with a for loop and also demonstrate using next() manually for the first 4 values. [10 marks] 

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n=int(input())

for num in fibonacci(n):
    print(num)
x=fibonacci(n)
print(next(x))
print(next(x)) 
print(next(x))
print(next(x))