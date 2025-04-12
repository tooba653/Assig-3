# Tuple
my_tuple = (10, "hello", 3.14, True)
print("Original tuple:", my_tuple)

# Immutable: cannot modify elements
try:
    my_tuple[1] = "new value"
except TypeError as e:
    print("TypeError (cannot modify tuple):", e)

# Cannot add or remove elements
try:
    my_tuple.append(5)
except AttributeError as e:
    print("AttributeError (cannot append):", e)

try:
    my_tuple.remove(10)
except AttributeError as e:
    print("AttributeError (cannot remove):", e)

# Accessing elements
print("\nFirst element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Tuple slicing
print("Sliced tuple (1:3):", my_tuple[1:3])

# Tuple length
print("Length of tuple:", len(my_tuple))

# Iterating through a tuple
print("\nIterating through tuple:")
for item in my_tuple:
    print("Item:", item)

# Checking if item exists in tuple
print("\nIs 10 in tuple?", 10 in my_tuple)
print("Is 'world' in tuple?", "world" in my_tuple)

# Concatenating tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2
print("\nConcatenated tuple:", combined)

# Repeating tuples
repeated = tuple1 * 3
print("Repeated tuple:", repeated)

# Unpacking tuple
person = ("Alice", 25, "Engineer")
name, age, job = person
print("\nUnpacked values:")
print("Name:", name)
print("Age:", age)
print("Job:", job)

# Nested tuple
nested = (1, (2, 3), (4, (5, 6)))
print("\nNested tuple:", nested)
print("Accessing nested element:", nested[2][1][0])