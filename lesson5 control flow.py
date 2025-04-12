# Comparison Operators
a = 10
b = 20
print("Is a equal to b?", a == b)
print("Is a not equal to b?", a != b)
print("Is a greater than b?", a > b)
print("Is a less than or equal to b?", a <= b)

# Logical Operators
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# The if Statement
num = 7
if num > 0:
    print("The number is positive")

# The else Statement
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# The elif Statement
marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C or below")

# Nested if Statement
age = 25
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage - Entry not allowed")