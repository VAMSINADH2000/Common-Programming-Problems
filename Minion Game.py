vow ="AEIOU"
STRING = "BANAASA"
def minion_game(string):
    c = v = 0
    for i in range(0, len(string)):
        if string[i] not in vow:
            print(string[i])
            # c = c + 1
            c = len(string) - i + c
        else:
            print(string[i])
            # v = v + 1
            v = len(string) - i + v
    # if v > c:
    #     print("Kevin", v)
    # elif v == c:
    #     print("Draw")
    # else:
    #     print("Stuart", c)
minion_game("BANAASA")

