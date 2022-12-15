# two sum

def two_sum(nums, target):
    myHash = {}

    for i in range(len(nums)):
        if (target - nums[i]) in myHash:
            return [myHash[target - nums[i]], i]
        myHash[nums[i]] = i
    return []


print(two_sum([2, 7, 11, 15], 9))
