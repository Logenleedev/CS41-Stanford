import sys

command = sys.argv[1]


list = []
i = 0
while True:
    number = float(input("Number: "))
    if (number == 0):
        print("Your numbers were:")
        while (i < len(list)):

            print(list[i])
            i += 1
        break
    list.append(number)


def sum_number(list):
    count = 0
    i = 0
    while i < len(list):
        count += list[i]
        i += 1
    return count
def average(list):
    nominator = sum_number(list)
    result = nominator/len(list)
    return result

def max_number(list):
    number = max(list)
    return number

def min_number(list):
    number = min(list)
    return number

if command == '-sum':
    print("The sum of those numbers is {}".format(sum_number(list)))
elif command == "-avg":
    print("The average of thos numbers is {}".format(average(list)))
elif command == '-max':
    print("The largest number is: {}".format(max(list)))
else:
    print("The largest number is: {}".format(min(list)))