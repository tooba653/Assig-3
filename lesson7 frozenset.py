#Creating a frozenset with duplicate values
frozen = frozenset([1, 2, 3, 2, 1])
print("Frozenset with unique elements:", frozen)  # Duplicates are automatically removed

#Frozenset is immutable (cannot add or remove elements)

#Frozenset is unordered
for item in frozen:
    print("Item in frozenset:", item)

# Frozenset is hashable and can be used as a dictionary key
my_dict = {frozenset([1, 2, 3]): "This is a key"}
print("Dictionary with frozenset key:", my_dict)