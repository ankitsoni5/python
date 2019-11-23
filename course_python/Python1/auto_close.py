path="D:\\ankit.txt"
with open(path) as ft:
    for line in ft:
        print(line.rstrip())

# Once the program is out of with block it will automatically close the connection.
# avoid manual close.