import sys
# Part I

number = int(sys.argv[1])
even = []
count = True
i = 2
while count:
    if len(even) < number:
        if (i % 2 == 0):
            even.append(i)
    else:
        count = False
    i += 1
j = 0
while j < len(even):
    print(even[j])
    j += 1

# Part II

number = int(sys.argv[1])
helper = int(sys.argv[2])
even = []
count = True
i = 2
while count:
    if len(even) < number:
        if (i % 2 == 0):
            if (helper == 0):
                helper = 0
                even.append(i)
            else:
                helper -= 1
    else:
        count = False
    i += 1
print(even)

'''    
j = 0
while j < len(even):
    print(even[j])
    j += 1
'''
