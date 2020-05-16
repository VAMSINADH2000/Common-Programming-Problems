from collections import deque
#
lst1 = [6, 2, 5, 4, 5, 1, 6]

def largerarea(lst):
    maxarea = 0
    i = 0
    index = deque()
    while i < len(lst):
        if len(index) > 0:
            if  len(index) == 0 or lst[i] >= lst[index[-1]]:
                index.append(i)
                i += 1
            else:
                top = index.pop()
                if len(index) == 0:
                    area = i * lst[top]
                else:
                    area = lst[top] * (i - (index[-1]) - 1)

                maxarea = max(area, maxarea)

    # while not len(index) == 0:
    #     top = index.pop()
    #     if len(index) == 0:
    #         area = i * lst[top]
    #     else:
    #         area = lst[top] * (i - (index[-1]) - 1)
    #
    #     maxarea = max(area, maxarea)
        else:
            index.append(i)

    return maxarea


print(largerarea(lst1))
