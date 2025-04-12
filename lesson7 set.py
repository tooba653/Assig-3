# Set with multiple data types
mixed_set = {1, 3.14, "hello", True}
print("Mixed Set:", mixed_set)

# The set is unordered
unordered_set = {10, 20, 30, 40, 50}
print("Unordered Set:", unordered_set)

# The set is unchangeable (elements cannot be changed, only added or removed)

immutable_set = {1, 2, 3}
immutable_set[0] = 100 


# Using union method or operator (|) to combine sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print("Union using method:", union_set)
union_operator = set_a | set_b
print("Union using operator:", union_operator)

#  Discard and remove methods
set_numbers = {1, 2, 3, 4, 5}
set_numbers.discard(3)  # Will not raise error if element is missing
print("After discard:", set_numbers)
set_numbers.remove(2)   # Will raise error if element is missing
print("After remove:", set_numbers)

# Set order can change dynamically
dynamic_set = {10, 20, 30}
print("Original Set:", dynamic_set)
dynamic_set.add(40)
print("After Adding 40:", dynamic_set)
dynamic_set.remove(10)
print("After Removing 10:", dynamic_set)

