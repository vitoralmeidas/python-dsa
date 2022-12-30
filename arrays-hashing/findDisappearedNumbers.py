from collections import Counter


def findDisappearedNumbers(nums):
    test = {}

    for i in range(1, len(nums) + 1):
        test[i] = 1 + test.get(i, 0)
    for j in nums:
        if j in test:
            test.pop(j)
    return test.keys()

# try the O(1) space complexity


print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(findDisappearedNumbers([1, 1]))
