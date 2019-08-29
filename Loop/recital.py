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
