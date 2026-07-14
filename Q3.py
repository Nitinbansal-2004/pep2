#  Write a Python program to:  Create a function that used *args to take monthly salary of any number
# of months -> calculate_tax(*salaries)  This function calculates tax for each month (10% of salary).
# Use lambda and map() to calculate the tax and store the taxes into a list  Add all the taxes in 
# the list and return the total tax from the function  Use exception handling while calculating tax 
# to ensure valid numeric salary entries. o Handle TypeError  Handle all other errors 

def calculate_tax(*salaries):
    try:
        taxes = list(map(lambda salary: float(salary) * 0.10, salaries))
        total_tax = sum(taxes)       
        return total_tax
    except TypeError:
        print(" enter valid numeric salary .")
    except Exception as e:
        print(e)
n=int(input("number of months: "))
salaries=[]
for i in range(n):
    salary=input("enter salary: ")
    salaries.append(salary)
print(calculate_tax(*salaries))