import sys
# Integer test

'''
while True:
    number = int(input("Integer: "))

    if (number >= 20 and number <= 200):
        print("%d passes the test!"%number)
    elif (number < 0 and (not(number % 2 == 0))):
        print("%d passes the test!"%number)
    elif (number == 0):
        print("Bye!")
        break
    else:
        print("%d fail the test!"%number)
'''


# Desk check

'''
t_num = 1  # the current triangular number to print out
step = 2   # the quantity added to `t_num`, to get the next triangular number
print('Hello!')
while True:
    if t_num % 2 == 0 or t_num % 5 == 0:
        print(t_num)
    if t_num >= 15:
        break
    t_num += step
    step += 1
'''

# Odd number
'''
i = 1

while (i < 101):
    if (i % 2 != 0):
        print(i)
    i += 1
'''

# Flow Chart
'''
num = 1
line = ""

while num <= 100:
    if (num == 99):
        line += str(num)
        break
    if (num % 2 != 0):
        line += str(num) + ', '
    num += 1
print(line)
'''

# Reading Errors
'''
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
difference = num1 - num2
print(difference)
print(sys.argv[0])
'''


