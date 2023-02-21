# Create a program to add two given lists using a lambda expression and map.
# Example:
#   [1, 2, 3]
#   [4, 5, 6]
#   [5, 7, 9]

l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(list(map(lambda x, y: x + y, l1, l2)))
