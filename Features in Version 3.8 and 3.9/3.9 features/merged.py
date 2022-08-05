# Before version 3.9
a = {'apple':1, 'pear':2}
b = {'orange':3}
merged = {**a, **b}
print(merged)
print(a)

c = {'apple':1, 'pear':2}
d = {'orange':3}
print(c.update(d))
print(c)

# From version 3.9
a = {'apple':1, 'pear':2}
b = {'orange':3}
merged = a | b
print(merged)
print(a)

c = {'apple':1, 'pear':2}
d = {'orange':3}
c |= d
print(c)
