def ZeroSumSubArray(lst1):
    Set = set()
    lst1.sort()
    summ = 0
    for i in lst1:
        summ = summ + i
        if summ in Set or summ == 0:
            return "Yes"
        Set.add(summ)
    return "NO"
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        print(ZeroSumSubArray(lst))

