import sys

flag = sys.argv[1]
integer_string = input("Enter some integers: ")
integer = integer_string.split(",")
if flag:
    if " 8" in integer:
        print("Your integers were: {}".format(integer))
        print("The number 8 is at {}".format(integer.index(" 8")))
    else:
        print("Your integers were: {}".format(integer))
        print("The number 8 is at index -1")

