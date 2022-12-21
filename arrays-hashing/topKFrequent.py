def topKFrequent(nums, k):
    # hash
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # bucket
    freq = [[] for i in range(len(nums) + 1)]

    for v, i in count.items():
        freq[i].append(v)

    # counting
    print(freq)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for j in freq[i]:
            res.append(j)
            if len(res) == k:
                return res


print(topKFrequent([1, 1, 1, 2, 3, 2], 2))
