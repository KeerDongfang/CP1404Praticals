numbers = [3, 1, 4, 1, 5, 9, 2]


# 1
numbers[0] = "ten"
print(numbers)

# 2
numbers[-1] = 1
print(numbers)

# 3
print(numbers[2: 7:])


# 4
if 9 in numbers:
    print("9 is an elements in the list.")
else:
    print("9 is not an elements in the list.")
