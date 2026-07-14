
#  Write a complete program that does all of the following:
# a) Create a list of at least 6 product dictionaries, each with: name, price, category, quantity
# b) Write a generator function low_stock(products, threshold=5) that yields products where quantity< threshold
# c) Write a generator function expensive_items(products, min_price=1000) that yields products above 
# the given price
# d) Use list comprehension to create a list of product names in UPPERCASE for a given category 
# e) Use map() and lambda to apply a 10% price increase to all products 
# f) Use filter() and lambda to show only products with quantity > 0 (in-stock items)
# h) Save the final updated inventory to 'inventory.json'. Read it back using read() and
# print total character count of the file. 
import json

class ProductNotFoundError(Exception):
    pass

products = [
    {"name":"Laptop","price":50000,"category":"Elec","quantity":5},
    {"name":"Mouse","price":500,"category":"Elec","quantity":10},
    {"name":"Book","price":300,"category":"Edu","quantity":2},
    {"name":"Phone","price":20000,"category":"Elec","quantity":1},
    {"name":"Pen","price":20,"category":"Edu","quantity":0},
    {"name":"Bag","price":1200,"category":"Fas","quantity":4}
]

def low_stock(products,threshold=5):
    for p in products:
        if p["quantity"]<threshold:
            yield p

def expensive_items(products,min_price=1000):
    for p in products:
        if p["price"]>min_price:
            yield p

for p in products:
    if p["category"]=="Elec":
        print(p["name"].upper())


products = list(map(lambda p: {
    "name": p["name"],
    "price": p["price"] * 1.1,
    "category": p["category"],
    "quantity": p["quantity"]
}, products))

p = filter(lambda p: p["quantity"] > 0, products)
print(list(p))


with open("inventory.json","w") as f:
    json.dump(products,f,indent=4)

with open("inventory.json","r") as f:
    data=f.read()
    print(data)
    print(len(data))