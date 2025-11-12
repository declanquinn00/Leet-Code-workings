def longestConsecutive(nums) -> int:
    lookup = set()
    max_val = 0

    for elem in nums:
        lookup.add(elem)

    for item in nums:
        consecutive = 1
        check_next = True
        while check_next:
            item += 1
            if item in lookup:
                consecutive += 1
            else:
                check_next = False

        if consecutive > max_val:
            max_val = consecutive

    return max_val


nums = [2,20,4,10,3,4,5]

longestConsecutive(nums)