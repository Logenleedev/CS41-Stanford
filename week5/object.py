def non(func):
    func("hi")
    return int
print(non(print)('42'))
