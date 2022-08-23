from collections import defaultdict


def groupAnagrams(strs):
    # default dic
    # it provides a default value
    # for the key that does not exists
    # O(n)

    # we are saving what chars the string has equal each other and how many of them too.
    ans = defaultdict(list)

    count = []
    for s in strs:
        count = [0] * 26  # a ... z
        for c in s:
            count[ord(c) - ord('a')] += 1
            # list are unhashable, cannot be 'key', 'cause they're mutable
        ans[tuple(count)].append(s)

    print(ans.values())

    # O(mnlogn)
    # m -> strs' length
    #  nlogn -> sorted() method
    # hashmap = {}
    # for st in strs:
    #     key = ''.join(sorted(st))
    #     if key not in hashmap:
    #         hashmap[key] = [st]
    #     else:
    #         hashmap[key] += [st]
    # return hashmap.values()


print(groupAnagrams(["eae", "aea", "tan", "ate", "nat", "bat"]))
