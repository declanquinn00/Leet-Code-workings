def isArraySpecial(nums):
    size = len(nums)
    if len(nums) > 1:
        for i in range(0, len(nums)-1):
            if nums[i]%2 == nums[i+1]%2:
                return False
        return True
    else:
        return True

nums = [1,2,3,4]
nums2 = [1]
nums3 = []
nums4 = [4,3,1,6]

print(isArraySpecial(nums))
print(isArraySpecial(nums2))
print(isArraySpecial(nums3))
print(isArraySpecial(nums4))