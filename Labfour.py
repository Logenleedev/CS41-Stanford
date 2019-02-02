from functools import reduce
import operator
'''


Map
Recall from class that map(func, iterable) applies a function over elements of an iterable.


'''


listone = ["12","-2","0"]
newlistone = list(map(int,listone))
# print(newlistone)

listtwo = ["hello","world"]
newlisttwoone = list(map(len,listtwo))
# print(newlisttwoone)

def reverse(L):
    return L[::-1]
newlisttwotwo = list(map(reverse,listtwo))
# print(newlisttwotwo)



'''


Filter
Recall from class that map(func, iterable) applies a function over elements of an iterable.


'''


listthree = ['12', '-2', '0']
newlist = list(map(int,listthree))

newlistthree = list(filter(lambda x: x>=0,newlist))
# print(newlistthree)

# print(operator.add(1, 2))
# print(operator.mul(3, 10))
# print(operator.pow(2, 3))



# def fact(n):
#     return functools.reduce(operator.mul, range(1, n+1))
# print(fact(3))

'''

words = ['pear', 'cabbage', 'apple', 'bananas']
min(words)  # => 'apple'
words.sort(key=lambda s: s[-1])  # Alternatively, key=operator.itemgetter(-1)
words  # => ['cabbage', 'apple', 'pear', 'bananas'] ... Why 'cabbage' > 'apple'?
max(words, key=len)  # 'cabbage' ... Why not 'bananas'?
min(words, key=lambda s: s[1::2])  # What will this value be?


'''


'''

Replacing Control Flow
The first thing that needs to go are control flow statements - if/elif/else. Luckily, Python, like many other languages, short circuits boolean expressions. This means that we can rewrite

if <cond1>:   func1()
elif <cond2>: func2()
else:         func3()
as the equivalent expression

(<cond1> and func1()) or (<cond2> and func2()) or (func3())
Recalling Python's rules for short-circuiting boolean expressions, why does the above expression (usually) result in the same output as the procedural control flow case?

Note: The above works if and only if all of the functions return truthy values. In order to guarantee that these expressions are actually the same, you might have to write something like the following, because all two-element tuples are truthy regardless of their content.

((<cond1> and (func1(), 0)) or (<cond2> and (func1(), 0)) or ((func1(), 0)))[0]


'''


#Example




'''

if score == 1:
    return "Winner"
elif score == -1:
    return "Loser"
else:
    return "Tied"

'''

echo = lambda arg: arg
result = lambda score: (score == 1 and echo("Winner")) or (score == -1 and echo("Loser")) or echo("Tied")

# print(result(-1))


it = iter(range(100))

import itertools
import operator

for el in itertools.permutations('XKCD', 2):
    print(el, end=', ')



def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)
print(say_whee)



# Put simply: decorators wrap a function, modifying its behavior.

# https://realpython.com/primer-on-python-decorators/

