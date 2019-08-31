import sys

'''
f = open("whale.txt", "r+")
list = f.readlines()
f.write("hello!\n")
f.write("hello!\n")
f.close()
'''
file_path = str(sys.argv[1])
starting_string = sys.argv[2]
f = open(file_path, "r+")
list = f.readlines()
f.close()

result = []
i = 0

while i < len(list):
    if list[i][0] == starting_string:
        result.append(list[i])
    i += 1

j = 0
while j < len(result):
    print(result[j], end="")
    j += 1

