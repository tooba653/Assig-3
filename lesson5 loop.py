# For loop
print("For loop from 1 to 5:")
for i in range(1, 6):
    print(i)

# While loop
print("\nWhile loop counting down from 5:")
count = 5
while count > 0:
    print(count)
    count -= 1

# For loop with else (no break)
print("\nFor loop with else (no break):")
for number in range(3):
    print("Trying number:", number)
else:
    print("Loop finished without break.")

# For loop with break (else skipped)
print("\nFor loop with break (else skipped):")
for number in range(5):
    print("Checking:", number)
    if number == 2:
        print("Found 2, breaking loop")
        break
else:
    print("This won't print because break occurred.")

# Searching with else
print("\nSearching for value in list using for-else:")
my_list = [1, 3, 5, 7]
target = 6
for item in my_list:
    if item == target:
        print("Found:", item)
        break
else:
    print("Item not found.")

# Controlling loops with break and continue
print("\nControlling loop with continue (skip even numbers):")
for i in range(6):
    if i % 2 == 0:
        continue
    print("Odd:", i)

print("\nUsing break to stop at 3:")
for i in range(6):
    if i == 3:
        break
    print("i:", i)

# Nested loops
print("\nNested loops (multiplication table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")