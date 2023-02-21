# Create a function ‘printargs’ that accepts any number of positional and keyword arguments,
# and that prints them back to the user.
#
# Print:
#   - the mean of the positional arguments, rounded to 2 decimals (tip: use round for this)
#   - the named arguments ordered alphabetically by key, in an ascending order,
#     on a single line, separated by commas (tip: use join for this).
#
# Example:
#   printargs(10, 20, 20, n=1, b=5, c=2)
#   Mean: 16.67
#   b=5, c=2, n=1

def printargs(*args, **kwargs):
    print("Mean: ", round(sum(args) / len(args), 2))
    print(', '.join(sorted([f"{k}={v}" for k, v in kwargs.items()])))


printargs(10, 20, 20, n=1, b=5, c=2)
