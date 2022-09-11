def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, len(charSet))
    return res


print(lengthOfLongestSubstring("abcbbac"))

"""
    create a set to grap char without repetition
    during the loop, check if the actual char is in the set
    and while this char is in charSet remove it and increse l
    if the char is not in the chartSet, add it.
    during the loop... keep updating the length, getting the max
    between the actual length and the charSet's after the while 
"""
