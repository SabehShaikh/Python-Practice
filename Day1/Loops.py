# Loops:

# range(start, stop, step)

# For Loop
for i in range(5):  # Iterates 5 times (0 to 4)
    print("Value of i: ", i)

# While Loop
j = 15
while j <= 20:
    print("value of j: ", j)
    j += 1

# break statement
for num in range(1, 11):
    if num == 5:
        break
    print(num)

# continue statement 
for k in range(1,5):
    if k == 3:
        continue
    print(k)