#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the freqQuery function below.
def freqQuery(queries, q):
    result = []

    d = defaultdict(int)
    for i in range(q):
        u = queries[i][0]
        v = queries[i][1]
        if u == 1:
            d[v] += 1
            continue
        elif u == 2:
            if v in d.keys():
                d[v] -= 1
            continue
        else:
            if v in d.values():
                print("1")
            else:
                print("0")





if __name__ == '__main__':
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    freqQuery(queries, q)








