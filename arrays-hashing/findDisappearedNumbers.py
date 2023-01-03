from collections import Counter

# def findDisappearedNumbers(nums):
#     test = {}

#     for i in range(1, len(nums) + 1):
#         test[i] = 1 + test.get(i, 0)
#     for j in nums:
#         if j in test:
#             test.pop(j)
#     return test.keys()

# the O(1) space complexity


def findDisappearedNumbers(nums):
    # mark existing values
    for n in nums:
        i = abs(n) - 1  # indexes' range (0, n - 1) / nums' range (1, n)
        nums[i] = -1 * abs(nums[i])
    ans = []
    for i, v in enumerate(nums):
        if v > 0:
            ans.append(i+1)  # i + 1 = n
    return ans


print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(findDisappearedNumbers([1, 1]))
