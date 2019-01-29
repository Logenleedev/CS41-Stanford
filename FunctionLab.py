import statistics

def print_two(a, b):
    print("Arguments: {0} and {1}".format(a, b))



# #********** Invalid:
# # print_two() # invalid
# # # print_two(41) #Invalid
# print_two(4, b=1)
# # print_two(4, 1, 1)
# # print_two(b=4, 1)
# # print_two(1, a=1)
# # print_two(4, 1, b=1)

# #********** Valid
# # print_two(a=4, b=1) 
# # print_two(4, 1) # Valid 4,1
# # # print_two(a=4, b=1)
# # print_two(b=1, a=4)

# # Write two more function calls.

# def print_two(*a):
#     print("Good Morning Agent",a[0])

# print(print_two("Jake","Jerry"))


def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
# keyword_args(5, 8) #a = 5, b = 8, c=X, d = None  VALID
# keyword_args(5, 2, d=8, c=4) VALID

'''
a: 5
b: 2
c: 4
d: 8
'''
# keyword_args(1, c=7) VALID



'''
Careful about the "TWO PARAMETER" problem

CAREFUL about ->  <-
'''




def variadic(*args, **kwargs):
    print("Positional:", args)

'''
# variadic(n=1, 2, 3)
# variadic(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'})
variadic({'a':5, 'b':'x'}, *{'c':5, 'd':'x'}, **{'a':5, 'b':'x'})
'''

# Uncomment the ones you want to run!
# variadic(2, 3, 5, 7)
# variadic(1, 1, n=1)

# variadic()
# variadic(cs="Computer Science", pd="Product Design")
# variadic(cs="Computer Science", cs="CompSci", cs="CS")
# variadic(5, 8, k=1, swap=2)

# variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'})
# variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'})



## Average

def average(*args):
    """Return the average of numeric arguments or None if no arguments are supplied."""
    # print(statistics.mean(args))
    temp = 0
    if len(args) == 0:
        return 0
    else:
        for x in args:
            temp += x
        return (temp/len(args))


# print(average())  # => None
# print(average(5))  # => 5.0
# print(average(6, 8, 9, 11)) 






# Function Nuances
# Return
# Predict the output of the following code snippet. Then, run the code to check your hypothesis.


def say_hello():
    print("Hello!")

# print(say_hello())  # => ? Hello!

def echo(arg=None):
    print("arg:", arg)
    return arg

# print(echo())  # => ? None
# print(echo(5)) # => ? 5
# print(echo("Hello")) # => ? Hello

def drive(has_car):
    if not has_car:
        # Please never actually signal an error like this...
        return "Oh no!"
    return 100  # miles

# print(drive(False))  # => ? Oh no
# print(drive(True))   # => ? 100






# Case 1
# x = 10

# def foo():
#     print("(inside foo) x:", x)
#     y = 5
#     print('value:', x * y)

# print("(outside foo) x:", x)
# foo()
# print("(after foo) x:", x)



# Case 2
x = 10

def foo():
    x = 8  # Only added this line - everything else is the same
    # print("(inside foo) x:", x)
    y = 5
    # print('value:', x * y)

# print("(outside foo) x:", x)
foo()
# print("(after foo) x:", x)




# Something fishy is going on here. Can you deduce what is happening?
def append_twice(a, lst=None):
    if lst is None:
        lst = []
    lst.append(a)
    lst.append(a)
    return lst
# Works well when the keyword is provided
# print(append_twice(1, lst=[4]))  # => [4, 1, 1]
# print(append_twice(11, lst=[2, 3, 5, 7]))  # => [2, 3, 5, 7, 11, 11]

# # But what happens here?
# print(append_twice(1))
# print(append_twice(2))
# print(append_twice(3))


## Successfully use the default value


def fib(n, cache={0: 1, 1: 1}):
   if n in cache:  # Note: starting values in the dictionary captures our base cases.
       return cache[n]
   out = fib(n-1) + fib(n-2)
   cache[n] = out
   return out

# print(fib(10))  # => 89
# print(fib.__defaults__[0])  # Access the cached dictionary.


'''
__defaults__ and __kwdefaults__
'''

def all_together(x, y, c=2, *nums, indent=True, spaces=4, **options): pass

# print(all_together.__defaults__)  # => (1, )
# all_together.__kwdefaults__  # => {'indent':True, 'spaces':4}



def my_function():
    """Summary line: do nothing, but document it.
        
    Description: No, really, it doesn't do anything.
    """
    print("Hello Word")
    pass

# print(my_function.__doc__)




'''

__code__

'''





def all_together2(x, y, z=1, *nums, indent=True, spaces=4, **options):
    """A useless comment"""
    print(x + y * z)
    print(sum(nums))
    for k, v in options.items():
        if indent:
            print("{}\t{}".format(k, v))
        else:
            print("{}{}{}".format(k, " " * spaces, v))
            
code = all_together2.__code__

# print(code.co_argcount)
# print(code.co_cellvars)
# print(code.co_code)
# print(code.co_consts)
# print(code.co_filename)
# print(code.co_firstlineno)
# print(code.co_flags)
# print(code.co_freevars)
# print(code.co_kwonlyargcount)
# print(code.co_lnotab)
# print(code.co_name)
# print(code.co_names)
# print(code.co_nlocals)
# print(code.co_stacksize)
# print(code.co_varnames)


'''

OVERRIGHT

'''

def nice(): print("You're awesome!")
def mean(): print("You're... not awesome. OOOOH")

# Overwrite the code object for nice
nice.__code__ = mean.__code__

print(nice())  # prints "You're... not awesome. OOOOH"