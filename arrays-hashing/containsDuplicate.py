def contains_duplicate(nums):
    # less code
    return len(set(nums)) != len(nums)
    myHash = set()
    for i in nums:
        if i in myHash:
            return True
        else:
            myHash.add(i)
    return False


print(contains_duplicate([1, 2, 3, 1]))
