# Create a function ‘add_any’ that accepts any number of numbers as positional arguments and prints the sum of those numbers.
# Example:
#   add_any(10, 20, 30, 40)
#   100

def add_any(*args):
    return sum(args)


print(add_any(10, 20, 30, 40))
