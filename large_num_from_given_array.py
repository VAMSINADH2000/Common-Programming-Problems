

def largenum(x,y):
    xy = x + y
    yx = y + x
    if int(xy)>int(yx):
        return 1
    return 0
test = int(input())
for i in range(test):
    n = input()
    final = ""
    lst =[x for x in input().split()]
    for i in range(len(lst)):
        for j in range(i,len(lst)):

            if not largenum(lst[i],lst[j]):
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    for i in lst:
        final = final +  i
    print(final)
    del final



