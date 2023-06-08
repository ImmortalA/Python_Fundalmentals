# We have a number of money denominations including 1, 2, 5, 10, 20, 50, 100, 200, 500.
# Write a program such that when entering an amount, the program will tell us the number of bills so that it is minimal. For example:
# The amount of money is 1234, we will print out:
# 500 bill: 2
# 200 bill: 1
# 100 bill: 0      # Do not print this line be cause the amount of bills is 0
# 50 bill: 0       # Do not print this line be cause the amount of bills is 0
# 20 bill: 1
# 10 bill: 1
# 5 bill: 0        # Do not print this line be cause the amount of bills is 0
# 2 bill: 2
# 1 bill: 0        # Do not print this line be cause the amount of bills is 0

amount_of_money = eval(input("Enter the amount of money: "))
sum = amount_of_money

bill_500 = sum // 500
sum -= 500*bill_500

bill_200 = sum // 200
sum -= 200*bill_200

bill_100 = sum // 100
sum -= 100*bill_100

bill_50 = sum // 50
sum -= 50*bill_50

bill_20 = sum // 20
sum -= 20*bill_20

bill_10 = sum // 10
sum -= 10*bill_10

bill_5 = sum // 5
sum -= 5*bill_5

bill_2 = sum // 2
sum -= 2*bill_2

bill_1 = sum

if(bill_500 > 0):
    print("500 bill: ", bill_500)
if(bill_200 > 0):
    print("200 bill: ", bill_200)
if(bill_100 > 0):
    print("100 bill: ", bill_100)
if(bill_50 > 0):
    print("50 bill: ", bill_50)
if(bill_20 > 0):
    print("20 bill: ", bill_20)
if(bill_10 > 0):
    print("10 bill: ", bill_10)
if(bill_5 > 0):
    print("5 bill: ", bill_5)
if(bill_2 > 0):
    print("2 bill: ", bill_2)
if(bill_1 > 0):
    print("1 bill: ", bill_1)
