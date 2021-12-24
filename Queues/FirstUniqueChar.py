# Given a string s, return the first unique character

def firstUniqChar(s) :
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for key, value in d.items():
        if value == 1:
            return s.index(key)

    return -1