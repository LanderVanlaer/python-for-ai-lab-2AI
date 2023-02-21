# Create a list words=[ 'apple', 'radar', 'php', 'python', 'R' ].
# Print the palindromes in the list using a lambda expression and filter.
#
# Output:
#   ['radar', 'php', 'R']

words = ['apple', 'radar', 'php', 'python', 'R']

print(list(filter(lambda x: x == x[::-1], words)))
