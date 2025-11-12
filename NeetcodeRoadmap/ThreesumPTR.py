def threeSum(nums):
    nums = sorted(nums)
    size = len(nums)
    result = []

    for i in range(0, size - 2):
        # we can get around the duplicate entries issue by adding this line
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # twosumtwo approach
        first = nums[i]
        ptr1 = i + 1
        ptr2 = size - 1
        while ptr1 < ptr2:
            added = first + nums[ptr1] + nums[ptr2]
            if added == 0:
                # append
                result.append([first, nums[ptr1], nums[ptr2]])
                break
            elif added > 0:
                ptr2 = ptr2 - 1
            elif added < 0:
                ptr1 = ptr1 + 1

    return result

nums =[0,0,0,0]
print(threeSum(nums))