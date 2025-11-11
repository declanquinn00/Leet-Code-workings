class Solution:
    def productExceptSelf(nums):
        total = 1
        result = [0 for i in range(0,len(nums))]
        for index, num in enumerate(nums):
            if num == 0:
                total = 1
                # calc index value
                for i in range(0,index): # this is actually done already!
                    total = total * nums[i]
                for i in range(index+1,len(nums)):
                    total = total * nums[i]

                result[index] = total
                return result

            else:
                # otherwise... calc all totals
                total = total * nums[index]

        # now divide by each element
        for index, num in enumerate(nums):
            div =  total // num
            result[index] = div

        return result
