def two_strings(s1,s2):
    s3 = set()
    s3 = s1.intersection(s2)
    if len(s3)!=0:
        return "YES"
    return "NO"
test = int(input())
for i in range(test):
    sets1 = set([ch for ch in input()])
    sets2 = set([ch for ch in input()])
    print(two_strings(sets1,sets2))
