def subarraySum(self, nums: List[int], k: int) -> int:
    res = 0
    currSum = 0
    prefixDict = {0: 1}

    for num in nums:
        currSum += num
        diff = currSum - k

        # add the prefix differences
        res += prefixDict.get(diff, 0)

        # add to dict
        prefixDict[currSum] = 1 + prefixDict.get(currSum, 0)

    return res