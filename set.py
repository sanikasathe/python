# Creating sets
set1 = {23, 2, 65, 78, 21}
set2 = {'mango', 2, 'orange'}

# Adding elements to sets
set1.add(50)        # Adds 50 to set1
set1.add(100)       # Adds 100 to set1
set2.add('grapes')  # Adds 'grapes' to set2

# Removing elements from sets
set1.remove(65)     # Removes 65 from set1
set1.discard(23)    # Removes 23 from set1 (does nothing if element is not found)
set1.remove(78)     # Removes 78 from set1

# Attempt to discard/remove an element not present in the set
set1.discard(14)    # Does nothing since 14 is not in set1
# set1.remove(20)   # Will raise a KeyError because 20 is not in set1

# Clearing sets
set1.clear()        # Clears all elements in set1
set2.clear()        # Clears all elements in set2

# Set union (merging two sets)
set = set1.union(set2)  # Returns a new set that contains elements from both set1 and set2
set = set1 | set2       # Alternate way to do union using the '|' operator
