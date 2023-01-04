def pivotIndex(nums):
    totalSum = sum(nums)  # it'll never change....
    leftSum = 0
    for i in range(len(nums)):
        # it'll always be the same calculation
        rightSum = totalSum - leftSum - nums[i]
        if leftSum == rightSum:
            return i
        leftSum += nums[i]

    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
