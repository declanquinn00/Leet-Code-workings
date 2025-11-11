def twoSum(self, nums: List[int], target: int) -> List[int]:
    hmap = {}
    # build the Hmap up as we go along
    for i in range(0, len(nums)):
        num = nums[i]
        res = target - num
        if res in hmap:
            minnum = min(i, hmap.get(res))
            maxnum = max(i, hmap.get(res))
            return [int(minnum), int(maxnum)]
        # add to hashmap
        hmap[num] = i
