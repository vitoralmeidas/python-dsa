def longestConsecutive(nums) -> int:

    numSet = set(nums)
    longest = 0

    for num in numSet:
        # (num - 1) will be a first number in a sequence, 1, 2,3 .... or 5, 6, 7
        if (num - 1) not in numSet:
            length = 0
            while (num + length) in numSet:
                length += 1
            longest = max(length, longest)

    return longest


print(longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
