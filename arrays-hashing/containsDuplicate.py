def containsDuplicates(nums) -> bool:

    return len(set(nums)) != len(nums)

    hashSet = set()
    for num in hashSet:
        if num in hashSet:
            return True
        hashSet.add(num)
    return False
