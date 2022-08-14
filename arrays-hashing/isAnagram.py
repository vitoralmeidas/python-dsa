from collections import Counter


def isAnagram(s, t):
    #  using a libary
    return Counter(s) == Counter(t)

    # easier to understand
    if len(s) != len(t):
        return False

    hashMap = {}

    for char in s:
        hashMap[char] = hashMap.get(char, 0) + 1

    for char in t:
        if char in hashMap:
            hashMap[char] = hashMap.get(char, 0) - 1
        else:
            return False

    for val in hashMap.values():
        if val != 0:
            return False

    return True

    # slower...
    return sorted(s) == sorted(t)


print(isAnagram('aacc', 'ccac'))
