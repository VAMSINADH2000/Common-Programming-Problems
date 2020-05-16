from itertools import permutations
from collections import Counter, defaultdict

s = 'abba'
n = 3
res = 0
d = defaultdict(int)
for i in range(1, len(s)):
    count = 0
    for j in range(len(s) - i + 1):
        a = "".join(sorted(s[j:j + i]))
        print(a)
        d[a] += 1
        res += d[a] - 1
        print(d, res)
