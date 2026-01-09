def subarraySum(self, nums: List[int], k: int) -> int:
    res = 0
    currSum = 0
    prefixDict = {0: 1}

    # create a prefix map and add the number of prefix occurrences
    # we want to obtain the amount of items in the dictionary could be included in our result
    # we check if the diff is available in the dictionary to see if there is a valid prefix solution here
    # important we build a we go along
    for num in nums:
        currSum += num
        diff = currSum - k

        # add the prefix differences
        res += prefixDict.get(diff, 0)

        # add to dict
        prefixDict[currSum] = 1 + prefixDict.get(currSum, 0)

    return res