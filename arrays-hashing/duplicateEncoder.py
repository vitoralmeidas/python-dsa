from collections import Counter
"""
    "(" if that character appears only once in the original string,
    or ")" if that character appears more than once in the original string
    
    
    "din"      =>  "((("
    "recede"   =>  "()()()"
    "Success"  =>  ")())())"
    "(( @"     =>  "))((" 
"""


def duplicateEnconder(word):
    # lower the letters before put in an array and then mapping the letter's occurrences
    word = word.lower()
    count = Counter(list(word.lower()))
    ans = ""
    print(count)
    for i in word:
        # check if there is more than one occurency for each letter
        if count[i] > 1:
            ans += ")"
        else:
            ans += "("
    return ans


print(duplicateEnconder("Success"))
