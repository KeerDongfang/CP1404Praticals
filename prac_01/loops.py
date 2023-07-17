"""
a.
for i in range(0,101,10):
    print(i, end=" ")
print()
"""
for i in range(0, 101, 10):
    print(i, end=" ")
print()

"""
b. 
for i in range(20,0,-1):
    print(i, end=" ")
print()
"""
for i in range(20, 0, -1):
    print(i, end=" ")
print()

"""
c. 
get number_of_star
for i in range(number_of_star)
    print(*, end='')
print()
"""
number_of_star = int(input("Number of stars:"))
for i in range(number_of_star):
    print('*', end='')
print()

"""
d.
get number_of_line
for i in range(number_of_line + 1)
    print('*'* i , end='/n')
print()
"""
number_of_line = int(input("Number of line:"))
for i in range(number_of_line + 1):
    print('*' * i)
print()
