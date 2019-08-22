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

# Odds again
'''
if (len(sys.argv)==1):
    print("Usage: python3 use -a | -b")
elif (sys.argv[1] == '-b'):
    i = 100
    while (i > 0):
        if (i % 2 != 0):
            print(i)
        i -= 1
else:
    i = 1
    while (i < 101):
        if (i % 2 != 0):
            print(i)
        i += 1
'''

#Eels part 1
'''
command = sys.argv[1:]
for i in range(len(command)):
    print(command[i])
'''

#Eels part 1
'''
command = sys.argv[1:]

i = 0
'''
# Use for loop
# for j in range(len(command)):
#     if (command[j] == 'eel' or command[j] == 'eels'):
#         i += 1
'''
counter = 0
while counter < len(command):
    if (command[counter] == 'eel' or command[counter] == 'eels'):
        i += 1
    counter += 1

if (i == len(command)):
    print("Wow you got so many eels here!")
elif (i > 0 and i < len(command)):
    print("there are a few eels")
else:
    print("where are eels?")
print(command)
'''

# Average

'''
a = []
while True:
    num = int(input())
    if (num == 0 ):
        break
    else:
        a.append(num)
print(sum(a)/len(a))
'''

#Modulo again
'''
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
remainder = num1 - num2*(num1//num2)
print(remainder)
'''

#Hailstones
'''
num = int(sys.argv[1])
answer = []
while (num != 1):
    if (num % 2 == 0):
        num = num/2
    else:
        num = num*3 + 1
    answer.append(num)
for n in range(len(answer)):
    print(answer[n], end=" ")
'''

# Prime
'''
num = int(input("One positive integer"))
is_prime = True
if num > 1:
    for n in range(2, num):
        if (num % n == 0):
            is_prime = False

if is_prime:
    print("Prime!")
else:
    print("not prime!")
'''
