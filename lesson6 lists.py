# List
my_list = [10, "hello", 3.14, 10, True]
print("Original list:", my_list)

# List is ordered and indexed
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# List slicing
print("Sliced (index 1 to 3):", my_list[1:4])

# Common list methods
my_list.append("new item")
print("\nAfter append:", my_list)

my_list.insert(2, "inserted")
print("After insert at index 2:", my_list)

my_list.extend([99, 100])
print("After extend:", my_list)

# Removing elements - by value
my_list.remove(10)  
print("\nAfter removing 10 (value-based):", my_list)

# Removing elements - remove returns None
result = my_list.remove("hello")  
print("Remove returns:", result)

# Removing elements - raises ValueError if value not found
try:
    my_list.remove("not-in-list")
except ValueError as e:
    print("ValueError:", e)

# pop method - index-based, returns removed item, raises IndexError
print("\nUsing pop():")
removed_item = my_list.pop(2)
print("Removed:", removed_item)
print("List after pop:", my_list)

try:
    print("Trying to pop from invalid index:")
    my_list.pop(100)
except IndexError as e:
    print("IndexError:", e)

# Sorting (default ascending)
numbers = [5, 2, 9, 1]
numbers.sort()
print("\nSorted ascending:", numbers)

# Descending order
numbers.sort(reverse=True)
print("Sorted descending:", numbers)

# Sorting by string length
words = ["apple", "banana", "kiwi", "fig"]
words.sort(key=len)
print("\nSorted by length:", words)

# Sorting by last character
words.sort(key=lambda word: word[-1])
print("Sorted by last character:", words)

# Reverse sorting
words.reverse()
print("Reversed list:", words)

# Iterating over list
print("\nIterating over list:")
for item in words:
    print("Item:", item)