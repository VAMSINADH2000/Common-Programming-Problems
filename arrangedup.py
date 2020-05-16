a = [2,2,1,5,4,2,3,3]
b = set()
c = []
for i in a:
    if i not in b:
        c.append(i)
        b.add(i)
print(c)