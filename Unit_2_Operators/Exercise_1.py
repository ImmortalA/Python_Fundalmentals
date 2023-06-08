# Enter 2 integer number and print out the sum, difference, product, quotient

number_1 = eval(input("Enter the 1st number: "))
number_2 = eval(input("Enter the 2nd number: "))

print("\n")

print("The sum of %d and %d is: %d" %(number_1, number_2, number_1 + number_2))
print("The difference of %d and %d is: %d" %(number_1, number_2, number_1 - number_2))
print("The product of %d and %d is: %d" %(number_1, number_2, number_1 * number_2))
print("The quotient of %d and %d is: %f" %(number_1, number_2, number_1 / number_2))