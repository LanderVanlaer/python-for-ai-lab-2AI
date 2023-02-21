# Create a function 'mysort' that accepts any number of positional arguments and one named argument ‘asc’,
# which has to be True by default (hence, this is a default argument). If asc is True,
# print the positional arguments in ascending order, otherwise, print them in descending order (print them
# on a single line, comma-separated.
#
# Tip: use list comprehension to convert the arguments to strings and join to print them comma-separated).
#
# Example:
#   mysort(10, 50, 40, 20, 30)
#   10, 20, 30, 40, 50
#
#   mysort(10, 50, 40, 20, 30, asc=False)
#   50, 40, 30, 20, 10

def mysort(*args, asc=True):
    print(', '.join([str(x) for x in sorted(args, reverse=not asc)]))


mysort(10, 50, 40, 20, 30)
mysort(10, 50, 40, 20, 30, asc=False)
