import sys


f = open("whale.txt", "r+")
list = f.readlines()
f.write("hello!\n")
f.write("hello!\n")
f.close()
# print(list)
# for n in range(len(list)):
#     print(list[n], end="")
# i = 0
# while i < len(list):
#     if (list[i][0] != )
