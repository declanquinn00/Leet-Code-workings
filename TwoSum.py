def twoSum(nums, target):
    for i in nums:
        num1 = nums[i]
        for j in nums:
            num2 = nums[j]
            if i!=j:
                if target == num1 + num2:
                    array = [i, j]
                    return array
    return None

nums = [0,1,2]
target = 3
array = twoSum(nums, target)
print(array)
