nums = [1,2,3,4,4,5]
nums2 = [1,1,1,1,1,1]
# Not using nums.remove()
def removeElement(nums, val):
    i = 0
    j = 0
    nums.sort()
    while i < len(nums):
        if (nums[i] == val):
            while nums[i] == val:
                i += 1
                if(i==len(nums)):
                    return j
        else:
            nums[j] = nums[i]
            j += 1
            i += 1
    return j

print(removeElement(nums, 4))
print(removeElement(nums2, 1))