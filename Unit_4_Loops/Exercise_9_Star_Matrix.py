# Enter the number of rows, the number of columns, print the star matrix
# Example:
# Enter number of rows: 3
# Enter number of columns: 4
# ****
# ****
# ****
# Note: use print(, end="") to print and "\n" to print new line

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(columns):
        print("*", end="")
    print("\n", end="")