from collections import deque


def maxSlidingWindow( nums, k: int):
    j = 0
    q = deque()
    res = []
    # plus one because its -1 due to the upperbound but we subtract a non ound
    for i in range(0, len(nums)-k + 1):
        target = i + k
        # popleft if too big
        if q and len(q) >= target:
            q.popleft()
        while j < target:
            if not q:
                q.append(nums[j])
            elif q[-1] < nums[j]:
                # pop all lesser vals to get decreasing order
                while q and q[-1] < nums[j]:
                    q.popleft()
                q.append(nums[j])
            else:
                q.append(nums[j])
            j += 1
        # now reset j to j + i
        # first in queue is our first res
        res.append(q[0])

    return res

nums = [1, 2, 1, 0, 4, 2, 6]
k = 3
print(maxSlidingWindow(nums,k))