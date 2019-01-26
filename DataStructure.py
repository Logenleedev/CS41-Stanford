 

# Fizz, Buzz, FizzBuzz!

def fizzbuzz(n):
    list = []
    for x in range (n):
        if x == 0:
            list.append(0)
        elif x%3 == 0 or x%5 == 0 :
            list.append(x)
        else:
            continue
    return sum(list)

# Collatz Sequence

def collatz_len(n):
    i = 1
    while n!=1:
        if n%2 == 0:
            n = n/2 
        else:
            n=3*n+1
        i = i +1
    return (i)


# Max collatz length

def max_collatz_len(n):
    list = [collatz_len(x) for x in range(1,n)]
    return max(list)



# Fahrenheit to Celsius converter

def convert_fahr_to_cels(FInput):
    FInput = float(input("Temperature F?"))
    COutput = (FInput-32)*0.5555555555555556
    return round(COutput,2)
'''
 print(convert_fahr_to_cels(10))
'''

# Zen printing


def print_tictactoe():
    print(" X","|",".","|",". ")
    print("-"*11)
    print(" .","|","O","|",". ")
    print("-"*11)
    print(" .","|","O","|","X ")

'''

s = [0] * 3
print(s)
s[0] += 1
print(s)

s = [''] * 3
print(s)
s[0] += 'a'
print(s)

s = [[]] * 3
print(s)
s[0] += [1]
print(s)

'''


def gcd(a,b):
    listA = []
    listB = []
    temptA = list(range(1,a+1))
    temptB = list(range(1,b+1))
    for x in temptA:
        if a%x == 0:
            listA.append(x)
    for x in temptB:
        if b%x == 0:
            listB.append(x)
    setA = set(listA)
    setB = set(listB)
    print(setA&setB)

# print([x for x in [1, 2, 3, 4]]) #[1,2,3,4]
# print([n - 2 for n in range(10)]) #[-2,-1,0,1,2,3,4,5,6,7]
# print([k % 10 for k in range(41) if k % 3 == 0]) # [0,3,6,9,2,5,8,1,4,7,0,3,6,9]
# print([s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]]) #['python']
# arr = [[3,2,1], ['a','b','c'], [('do',), ['re'], 'mi']]
# print([el.append(el[0] * 4) for el in arr])  # What is printed?
# print(arr)
'''
[0, 1, 2, 3] -> [1, 3, 5, 7]  # Double and add one
'''
# oldlist = [0,1,2,3]
# newList = [x*2+1 for x in oldlist]
# print(newList)
'''
['apple', 'orange', 'pear'] -> ['A', 'O', 'P']  # Capitalize first letter
'''

# oldlist = ['apple','orange','peer']
# newlist = [x[0][0].upper() for x in oldlist]
# print(newlist)

'''
['apple', 'orange', 'pear'] -> ['apple', 'pear']  # Contains a 'p'
'''

# oldlist = ['apple','orange','pear']
# def filter(oldlist):
#     newlist = []
#     for x in oldlist:
#         if 'p' in x:
#             newlist.append(x)
#     return newlist
# print(filter(oldlist))