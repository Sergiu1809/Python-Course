# Given a list of numbers [3, 1, 4, 1, 5, 9, 2, 6, 5] — find the unique numbers using a set, then sort them into a list.

list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
set = set()

for item in list:
    set.add(item)

print(set)
