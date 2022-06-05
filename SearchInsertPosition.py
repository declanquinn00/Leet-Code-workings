def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    r = len(nums)-1

    while l <= r:
        m = (l+r)//2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            l = m + 1
        else:
            r = m - 1
    else:
        return l