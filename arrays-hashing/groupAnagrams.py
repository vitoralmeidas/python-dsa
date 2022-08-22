from collections import defaultdict


def groupAnagrams(strs):
    #  default dic
    # it provides a default value
    # for the key that does not exists
    res = defaultdict(list)

    count = []
    for s in strs:
        count = [0] * 26  # a ... z
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)

    return res.values()

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


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
