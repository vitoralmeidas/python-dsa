from collections import Counter

"""
Input: text = "nlaebolko"
Output: 1

Input: text = "loonbalxballpoon"
Output: 2

Input: text = "leetcode"
Output: 0
"""


def maxNumberOfBalloons(text: str):
    countText = Counter(text)
    ballon = Counter("balloon")

    # getting the ratios between the hashs
    # looking for the min, because we have a bottlerneck to look for
    # b = 1, a = 1, l = 2, o = 2, n = 1
    # we can make the word at most once with the values
    # if we have more than the min, we will set the max times that we can create the word
    # seeing the letter which appers less
    # b = 2, but a = 1, so we will have just one complete word
    # because of that we are looking for the min
    # we need a big number to compare it, because our value (big number) wont be replaced

    # + Infinity = float("inf") -> min  // - Infinity =  float("-inf") -> max
    res = len(text)

    for c in ballon:
        res = min(res, countText[c] // ballon[c])

    return res


print(maxNumberOfBalloons("loonbalxballpoon"))
