test = int(input())
ord = '! # $ % & * @ ^ ~ '.split()
for i in range(test):
    n = int(input())
    nuts = input()
    bolts = input()
    nuts = nuts.split()
    bolts = bolts.split()
    pat = ""
    for i in ord:
        if i in nuts and i in bolts:
            pat = pat + i + " "
    print(pat)
    print(pat)

