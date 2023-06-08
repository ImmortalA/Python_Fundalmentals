# Enter an integer. Check if the integer is prime or not?
flag = 0

n = int(input("Enter an integer: "))

if (n < 2):
    print("%d is not a prime number" % n)
elif (n == 2):
    print("%d is a prime number" % n)
else:
    for i in range(2, int(n**1/2 + 1)):
        if (n % i == 0):
            flag = 1
            break
    if (flag == 1):
        print("%d is not a prime number" % n)
    else:
        print("%d is a prime number" % n)