nums1 = [1,2,2,3,4,5]
nums2 = None
nums3 = [1,1,2]
nums4 = [0,0,1,1,1,2,2,3,3,4]
def removeDuplicates(nums):
    k = 0  # count duplicates
    if (nums != None):
        l = len(nums)
        i = 1
        prev = nums[0]
        while i < l:
            if (nums[i] == prev and nums[i]!= None):
                j = i
                nums[i] = None
                k = k + 1
                while j < l - 1:
                    nums[j] = nums[j + 1]
                    j = j + 1
                if j == l - 1 and nums[j] != None:
                    nums[j] = None
                    j = j + 1
            else:
                prev = nums[i]
                i = i + 1
        k = l - k  # length - duplicates = sorted array length
    return k

print(removeDuplicates(nums1))
print(removeDuplicates(nums2))
print(removeDuplicates(nums3))
print(removeDuplicates(nums4))
print("Done")