# Enter 2 float number x and n, calculate and print out the result of the function below:
# (x^2 + 6x + 1)(n^3 + 6n)

x = eval(input("Enter the x number: "))
n = eval(input("Enter the n number: "))

result = (x**2 + 6*x + 1)*(n**3 + 6*n)

print("(x^2 + 6x + 1)(n^3 + 6n) =", result)
