def topKFrequent(nums, k):
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    freq = [[] for i in range(len(nums) + 1)]

    for v, i in count.items():
        # i count, v actual numbers in nums
        freq[i].append(v)

    ans = []
    # backwards loop, because the tops are the last ones
    # range(last_elemenet, until_index, loop_order)
    for j in range(len(freq) - 1, 0, -1):
        # checking all elements in the inner arrays
        for i in freq[j]:
            ans.append(i)
            # make sure that the result will stop when we already have the K-Tops
            if len(ans) == k:
                return ans


print(topKFrequent([1, 1, 1, 2, 3, 2], 2))
