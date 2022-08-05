def raised_to(x, y, /, z = None):
    w = x ** y
    if z is not None:
        w %= z
    return w
print(raised_to(3, 5, z = 6))
print(raised_to(3, 5, 6))

'''
/ is called positional only argument operator
parameter before / can be passed as positional only
parameter after / can be passed as positional as well as with keywords
'''
