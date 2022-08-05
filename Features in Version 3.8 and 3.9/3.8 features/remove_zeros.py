# WAP using list comprehension and walrus operator to separate zeros from a list
data = [0, 5, 4, 0, 3, 2, 1, 0]
print([res for n in data if (res := int(n)) != 0])

'''
data = [0, 5, 4, 0, 3, 2, 1, 0]
res = []
for n in data:
    if n != 0:
        res.append(n)
print(res)
'''
