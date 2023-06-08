# Enter a positive integer with exactly 3 digits. Calculate and print the reverse number.
# Example: Input: 523, Output: 325

# --- 1 ---
number = int(input("Enter a 3-digit number: "))

units = number % 10
tens = (number % 100 - units) / 10
hundreds = (number % 1000 - units - tens * 10) / 100
reverse_number = units * 100 + tens * 10 + hundreds

print("The reverse number is: %d" % reverse_number)

# --- 2 ---
# number = int(input("Enter a 3-digit number: "))
# reverse_number = 0

# units = number % 10
# number = number % 100
# reverse_number = reverse_number*10 + units

# units = number % 10
# number = (number - units) / 10
# reverse_number = reverse_number*10 + units

# units = number % 10
# number = (number - units) / 10
# reverse_number = reverse_number*10 + units

# print("The reverse number is: %d" % reverse_number)


# --- 3 ---
# number = input("Enter a 3-digit number: ")
# print("The reverse number is: %s%s%s" % (number[2], number[1], number[0]))


