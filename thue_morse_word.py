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

string = gen_string(6)

print(string[0])
print("---" + string[1])

def gen_empty_locs(k):

    list_blanks = []

    idx = 0
    for i in range(k):
        if i % 2 == 1:
            idx = length(i) + 1
            list_blanks.append(idx)
        
        else:
            idx += length(i)
            list_blanks.append(idx)
        

    return list_blanks[1:]

def gen_list(k, idx):
    if k < 2:
        return 0;
    elif k == 2:
        return [idx + 3]
    elif k % 2 == 1:
        l1 = gen_list(k - 1, idx)
        val = length(k - 1)
        l2 = [d + val for d in l1]

        l1.extend(l2)

        return l1
    else:
        val = length(k if k % 2 == 1 else k - 1) + 1 + idx
        l1 = gen_list(k - 1, idx)
        l2 = [val]
        l2.extend(gen_list(k - 1, val))
        l1.extend(l2)

        return l1

for i in range(1, 7):
    print(length(i))
    print(gen_list(i, 0))

l1 = gen_list(6, 0)
l2 = gen_list(6, 0)

for i in range(1, length(6)):
    l3 = [v - i for v in l2]

    last_val = l3[-1]
    s = set(l3)

    count = 0

    for v in l1:
        if v > last_val:
            break
        
        if v in s:
            count += 1
        else:
            count += 2
    print(l1)
    print(l3)
    print(length(6) - count - i)
    
# test


print(l1)
print(l2)