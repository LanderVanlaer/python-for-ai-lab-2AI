# Generate a list 'list1' with 10 random numbers from 0 to 10 using list comprehension.
# Generate a list 'list2' with 10 random numbers from 0 to 10 using list comprehension.
#
# Print the intersection of both lists using a lambda expression and filter.
#
# Example:
#   [7, 5, 2, 1, 1, 6, 9, 1, 2, 5]
#   [0, 4, 5, 2, 6, 4, 10, 3, 3, 10]
#   [5, 2, 6]
import random

list1 = [random.randint(0, 10) for _ in range(10)]
list2 = [random.randint(0, 10) for _ in range(10)]

print(list1)
print(list2)
print(list(filter(lambda n: n in list2, list1)))
