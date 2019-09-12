def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

print(swap(3, 5))
print("a is {}".format(swap(3, 5)[0]))
print("b is {}".format(swap(3, 5)[1]))
