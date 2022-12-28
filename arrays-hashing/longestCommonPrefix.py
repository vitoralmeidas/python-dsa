def longestCommonPrefix(strs):
    prefix = ""
    if strs == None or len(strs) == 0:
        return prefix

    # pointer to indicate what index we're at the strings
    for i in range(len(strs[0])):  # go through every single char of the first string
        # iterate through string to make sure all the string have the exact same char at index i
        for s in strs:
            # if the string -> s is shorter than the string we're looking for
            if i == len(s) or s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]

    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
