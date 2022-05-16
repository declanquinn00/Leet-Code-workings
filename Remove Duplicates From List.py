nums1 = [1,2,2,3,4,5]
nums2 = None
nums3 = [1,1,2]
nums4 = [0,0,1,1,1,2,2,3,3,4]
def removeDuplicates(nums):
    if(nums!=None):
        j = 1 # j can never be a duplicate
        for i in range(1,len(nums)):    # for each number
            if nums[i-1] != nums[i]:    # if not a duplicate
                nums[j] = nums[i]       # first set of numbers
                j += 1                  # increace non duplicate list
        return j
    else:
        return None

print(removeDuplicates(nums1))
#print(removeDuplicates(nums2))
print(removeDuplicates(nums3))
print(removeDuplicates(nums4))
print("Done")