def singleNumber(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        dictionary = {}
        for element in nums:
            tmpArray = []
            if dictionary.get(element) == None:
                tmpArray.append(element)
                dictionary[element] = tmpArray
            elif dictionary.get(element) != None:
                tmpArray = dictionary.get(element)
                tmpArray.append(element)
                dictionary[element] = tmpArray

        for key in dictionary:
            object = dictionary[key]
            if len(object) == 1:
                return object[0]

nums = [1,1,2,3,2]
singleNumber(nums)