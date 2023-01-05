from collections import Counter


class Solution:
    def isIsomorphic(s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            charS, charT = s[i], t[i]
            if ((charS in mapST and mapST[charS] != charT) or
                    (charT in mapTS and mapTS[charT] != charS)):
                return False
            mapST[charS] = charT
            mapST[charT] = charS

        return True


print(Solution.isIsomorphic("bbbaaaba", "aaabbbba"))
print(Solution.isIsomorphic("egg", "add"))
