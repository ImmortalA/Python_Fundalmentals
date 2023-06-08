# Enter two real numbers a, b. Calculate and solve the first degree equation: ax + b = 0.

print("ax + b = 0 - First Degree Equation Solver")

a = eval(input("Enter a: "))
b = eval(input("Enter b: "))

if (a == 0):
    if (b == 0):
        print("Infinite solutions")
    else:
        print("No solution")
else:
    print("x =", -b / a)