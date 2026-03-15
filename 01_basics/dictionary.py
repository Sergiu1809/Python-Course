# Ex1

dictionary = {
    "name": "apple",
    "price": 10,
    "stock": 50
}

print(dictionary["name"])
print(dictionary["price"])
print(dictionary["stock"])

dictionary["price"] = 20

print(dictionary["price"])

# Create a dict of 3 students with their grades. Loop through it and print "Alex: PASS" or "Alex: FAIL" based on grade ≥ 50.

dictionary1 = {
    "Alex": 20,
    "John": 60,
    "Andrei": 50
}

for key, value in dictionary1.items():
    if value >= 50:
        print(f"{key}: PASS")
    else:
        print(f"{key}: FAIL")
