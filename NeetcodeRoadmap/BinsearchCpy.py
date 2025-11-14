def binSearch(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + ((r - l) // 2)

        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid

    return - 1

print(binSearch(nums = [2,4,8,10,11],target = 10 ))
