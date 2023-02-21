# Using a lambda expression in list comprehension, print the table of 5.
#
# Output:
#   5
#   10
#   15
#   20
#   25
#   30
#   35
#   40
#   45
#   50

print(*[(lambda y: y * 5)(x) for x in range(1, 11)], sep="\n")
