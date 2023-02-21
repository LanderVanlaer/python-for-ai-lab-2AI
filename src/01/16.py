# Convert the sentence 'This is just a test sentence' into a list of words using strip.
# Print the number of unique characters for every word in that list using a lambda expression and map.
#
# Output: [4, 2, 4, 1, 3, 5]

print(list(map(lambda w: len([c for i, c in enumerate(w) if w.find(c) == i]),
               "This is just a test sentence".split(' '))))
