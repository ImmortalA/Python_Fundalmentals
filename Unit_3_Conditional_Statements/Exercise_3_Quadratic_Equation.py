# Enter three real numbers a, b, c.
# Calculate and print the solution of the quadratic equation: ax^2 + bx + c = 0.

print("ax^2 + bx + c = 0 - Quadratic Equation Solver")

a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))

if (a == 0):
    if (b == 0):
        if(c == 0):
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        print("x =", -b/a)
else:
    discriminant = b**2 - 4*a*c

    if (discriminant == 0):
        print("x =", -b / (2*a))
    elif (discriminant > 0):
        print("x1 =", (-b + discriminant**1/2) / (2*a))
        print("x2 =", (-b - discriminant**1/2) / (2*a))
    else:
        r = -b / (2*a)
        i = (-discriminant)**1/2 / (2*a)
        x1 = complex(r, i)
        x2 = complex(r, -i)

        print("x1 =", x1)
        print("x2 =", x2)
