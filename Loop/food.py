import sys

file_path = str(sys.argv[1])
f = open(file_path, "r+")
list = f.readlines()
f.close()

i = 0
while i < len(list):
    name = list[i].split(" ")[0]
    price = list[i].split(" ")[1]
    print(name)
    print(price)
    i += 1