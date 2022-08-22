def topKFrequent(nums, k):
    num_dic = {}
    ans = []
    for num in nums:
        if num in num_dic:
            num_dic[num] += 1
        else:
            num_dic[num] = 1

    # sorting..
    sorted_num_dic = sorted(num_dic.items(), key=lambda x: x[1], reverse=True)

    return print([x[0] for x in sorted_num_dic[:k]])


topKFrequent([1, 1, 1, 2, 3, 2], 2)
