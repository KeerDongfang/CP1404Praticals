numbers = []
print("Please enter 5 numbers.")
for i in range(5):
    number = float(input("Number :"))
    numbers.append(number)

average_of_numbers = sum(numbers)/len(numbers)

print(f"The first numer is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {average_of_numbers}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Please enter your username")

if username in usernames:
    print("Access granted.")
else:
    print("Access denied.")
