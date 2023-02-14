# Define two lists: one containing some countries, the other containing their capitals.
# Use the zip() method to merge them into one list of tuples (country, capital).
#
# Example:
#   co = ['Belgium', 'France', 'Greece']
#   ca = ['Brussels', 'Paris', 'Athens']
#   [('Belgium', 'Brussels'), ('France', 'Paris'), ('Greece', 'Athens')]

co = ['Belgium', 'France', 'Greece']
ca = ['Brussels', 'Paris', 'Athens']

print(list(zip(co, ca)))
