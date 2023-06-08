# Enter the number of rows, the number of columns, print the increasing number matrix
# Example:
# Enter number of rows: 3
# Enter number of columns: 4
# 1       2       3       4
# 1       2       3       4
# 1       2       3       4


# 1       1       1       1
# 2       2       2       2
# 3       3       3       3
# Note: use print(, end="\t") to print and "\n" to print new line

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(columns):
        print(j + 1, end="\t")
    print("\n", end="")

print("\n")

for i in range(rows):
    for j in range(columns):
        print(i + 1, end="\t")
    print("\n", end="")