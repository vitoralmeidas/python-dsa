def isSubsequence(s, t):
    # two pointers
    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return True if len(s) == i else False
