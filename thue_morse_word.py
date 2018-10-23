def length(k):
    if k == 0:
        return 1
    elif k % 2 == 1:
        return 2*length(k - 1)
    else:
        return 2*length(k - 1) + 1


def gen_string(k):
    string1 = ""
    string2 = ""

    l = length(k)

    for i in range(l // 2):
        string1 += "10"
        string2 += "01"

    if l % 2 == 1:
        string1 += "1"
        string2 += "0"

    return [string1, string2]

print(gen_string(6))