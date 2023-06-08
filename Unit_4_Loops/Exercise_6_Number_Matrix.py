# Enter the number of rows, the number of columns, print the increasing number matrix
# Example:
# Enter number of rows: 3
# Enter number of columns: 4
# 1       2       3       4
# 5       6       7       8
# 9       10      11      12
# Note: use print(, end="\t") to print and "\n" to print new line


rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

count = 0

for i in range(rows):
    for j in range(columns):
        count += 1
        print(count, end="\t")
    print("\n", end="")