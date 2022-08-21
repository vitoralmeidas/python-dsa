def groupAnagrams(strs):
    hashmap = {}
    for st in strs:
        key = ''.join(sorted(st))
        if key not in hashmap:
            hashmap[key] = [st]
        else:
            hashmap[key] += [st]
    return hashmap.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
