stri = "AABBCCDD"
k = 4
n = len(stri)
div = int(n / k)
lst = [i for i in stri]
for j in range(0,len(lst),div):
    str1 = ''
    str1 = str1 + "".join(((lst[j:j + div])))
    output = ""
    for i in str1:
        if i not in output:
            output += i
    print(output)
    del str1
    del output







