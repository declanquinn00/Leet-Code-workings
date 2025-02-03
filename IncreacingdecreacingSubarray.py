

def longestMonotonicSubarray(nums):
    if not nums:
        return 0

    # calc increacing
    max_inc = 0
    count = 1
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            count += 1
        else:
            if max_inc < count:
                max_inc = count
            count = 1
    if max_inc < count:
        max_inc = count

    # calc decreacing
    max_dec = 0
    count = 1
    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            count += 1
        else:
            if max_dec < count:
                max_dec = count
            count = 1
    if max_dec < count:
        max_dec = count
    # max increacing/derceacing
    return max(max_dec,max_inc)




nums = [3,3,3,3]
nums1 = [3,2,1]
nums2 = [1,4,3,3,2]
nums3 = []

print(longestMonotonicSubarray(nums1))