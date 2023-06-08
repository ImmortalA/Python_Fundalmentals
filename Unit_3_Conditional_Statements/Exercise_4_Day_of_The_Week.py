# Enter three integers d, m, y as day, month, year.
# Print out what day of the week it is.
# Use the following formula to convert the day, month, and year into the day of the week:
# A = int(d + 2*m + 3*(m + 1)/5 + y + (y/4) - (y/100) + (y/400) + 2)

# With the convention that January and February of year y are considered as months 13 and 14 of year y–1
# The day of the week will be determined by finding the remainder of the division A by 7
# The remainder is 0: Saturday
# The remainder is 1: Sunday
# The remainder is 2: Monday
# ...

d = int(input("Enter the day: "))
m = eval(input("Enter the month: "))
y = eval(input("Enter the year: "))

A = int(d + 2*m + 3*(m + 1)/5 + y + (y/4) - (y/100) + (y/400) + 2)
remainder = A % 7

if (remainder == 0):
    print("%d/%d/%d"%(d, m, y) + " is Saturday")
elif (remainder == 1):
    print("%d/%d/%d"%(d, m, y) + " is Sunday")
elif (remainder == 2):
    print("%d/%d/%d"%(d, m, y) + " is Monday")
elif (remainder == 3):
    print("%d/%d/%d"%(d, m, y) + " is Tuesday")
elif (remainder == 4):
    print("%d/%d/%d"%(d, m, y) + " is Wednesday")
elif (remainder == 5):
    print("%d/%d/%d"%(d, m, y) + " is Thursday")
else:
    print("%d/%d/%d"%(d, m, y) + " is Friday")