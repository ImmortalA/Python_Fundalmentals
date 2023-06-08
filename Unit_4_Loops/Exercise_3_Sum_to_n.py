# Enter an integer n >= 1, calculate the sum from 1 to n

n = 0
sum = 0

while n < 1:
    n = int(input("Enter an integer: "))
    if (n < 1):
        print("Invalid number, enter n >= 1")

for i in range(1, n + 1):
    sum += i

print("Sum from 1 to n is:", sum)