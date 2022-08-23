def containsDuplicates(nums) -> bool:
    hashset = set()

    for num in nums:
        if num in hashset:
            return False
        hashset.add(num)
    return True
