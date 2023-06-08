# Enter a positive integer, print the reverse of that number

n = -1
reverse_number = 0

while n < 0:
    n = int(input("Enter an integer: "))
    if (n < 0):
        print("Invalid number, enter n >= 0")

while (n > 0):
    digit = n % 10
    reverse_number = reverse_number*10 + digit
    n = n // 10

print("Reverse number =", reverse_number)
