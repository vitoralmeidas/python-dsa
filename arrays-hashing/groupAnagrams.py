from collections import defaultdict


def groupAnagrams(strs):
    # default dic
    # it provides a default value
    # for the key that does not exists
    # O(n)

    # we are saving what chars the string has equal each other and how many of them too.
    # we start with List <type> because, tuple does not have 'append()' method
    ans = defaultdict(list)

    count = []
    for s in strs:
        count = [0] * 26  # a ... z
        for c in s:
            # checking for same index ... [ord('e') - ord('a')] will be an index of count, so we'll change the actual value, adding 1
            count[ord(c) - ord('a')] += 1
            # list are unhashable, cannot be 'key', 'cause they're mutable
        ans[tuple(count)].append(s)

    print(ans.values())


print(groupAnagrams(["tae", "eat", "tan", "ate", "nat", "bat"]))
