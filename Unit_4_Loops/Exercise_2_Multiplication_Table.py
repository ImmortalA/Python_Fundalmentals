# Enter an integer n, print the multiplication table of n

n = int(input("Enter an integer: "))

for i in range(1, 11):
    print("%d * %d = %d"%(n, i, n*i))