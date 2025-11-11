def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(0, len(nums)+1)]
    result = []

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    # Bucket sort hack! append just the key in the value slot
    for key, val in count.items():
        freq[val].append(key)

    # now read off the last k keys
    for i in range(len(nums), 0,-1):
        for val in freq[i]:
            result.append(val)
            if len(result) == k:
                return result


nums = [7,7]
k = 1

res = topKFrequent(nums,k)
print(res)