# Generate a list of numbers from 0 to 9 using list comprehension.
# Using a lambda expression and map, print the square of those values in a list.
#
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

l = [x for x in range(0, 10)]

print(list(map(lambda x: x ** 2, l)))
