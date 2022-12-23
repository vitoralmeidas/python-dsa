def removeElement(nums, val):
    def keys(val):
        return val

    for i in sorted(nums, key=keys, reverse=False):
        if i == val:
            idx = nums.index(val)
            nums.pop(idx)
    return len(nums)

    """
        counting how many times we had to place the different elements of val
        at the beginning of the array
        by doing this we will return the length of "new array" if we have cut the occurrences of
        val in the array
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
