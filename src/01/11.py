# Generate a list of numbers from 0 to 9 using list comprehension.
# Create a lambda expression to check for even numbers, filter
# those values out (using filter of course) and print them as a list.
#
# Output: [0, 2, 4, 6, 8]

print(list(filter(lambda x: not x % 2, range(0, 9))))
