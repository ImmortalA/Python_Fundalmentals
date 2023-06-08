# Enter the 3 sides of the triangle. Calculate and print the perimeter and area according to the following formula:
# Perimeter = a+b+c
# Area = (p*(p-a)*(p-b)*(p-c))^1/2
# where p is the half perimeter.

a, b, c = eval(input("Enter the 3 sides of the triangle: "))

perimeter = a+b+c
p = perimeter / 2
area = (p*(p-a)*(p-b)*(p-c))**1/2

print("Perimeter:", perimeter)
print("Area:", area)
