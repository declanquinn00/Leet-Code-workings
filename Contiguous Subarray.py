nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    curr_max = overall_max = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        curr_max = max(curr_max + num, num)
        overall_max = max(overall_max, curr_max)

    return overall_max

print(maxSubArray(nums))