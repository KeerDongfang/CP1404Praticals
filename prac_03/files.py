# question 1:
out_file = open("name.txt", "w")
name = input("What is your name:")
print(name, file=out_file)
out_file.close()

# question 2:
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is ", name)

# question 3:
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
totals = number1 + number2
print(totals)
in_file.close()

# question 4:
totals = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    totals += number
print(totals)
in_file.close()
