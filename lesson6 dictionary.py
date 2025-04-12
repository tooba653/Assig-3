# Creating a dictionary to store person details
person = {
    "name": "Tooba",
    "age": 20,
    "profession": "Engineer"
}
print("Original dictionary:", person)

# Accessing values
print("\nAccessing values:")
print("Name:", person["name"])
print("Age:", person.get("age"))

# Modifying a dictionary
person["age"] = 29
person["city"] = "New York"
print("\nModified dictionary:", person)

# Deleting items
del person["profession"]  # Removes a key-value pair
print("\nAfter deleting 'profession':", person)

# Dictionary methods
print("\nDictionary keys:", person.keys())
print("Dictionary values:", person.values())
print("Dictionary items:", person.items())

# clear() method 
 #person.clear()
#print("After clear:", person)

# update() method
person.update({"email": "alice@example.com", "age": 30})
print("After update:", person)

# Iterating over dictionary
print("\nIterating over dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# Common pitfalls
print("\nCommon Pitfalls:")
# Accessing a non-existent key with [] will cause KeyError
try:
    print(person["salary"])
except KeyError as e:
    print("KeyError:", e)

# get() returns None or default value if key not found
print("Using get() for non-existent key:", person.get("salary", "Not Available"))

# Dictionary comprehension
print("\nDictionary Comprehension:")
squares = {x: x*x for x in range(1, 6)}
print("Squares dictionary:", squares)