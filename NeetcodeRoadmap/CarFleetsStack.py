def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    # pair = [[p,s] for p,s in zip(target,position)] # quick combination
    fleets = 0
    # hash map
    pairs = {}
    stack = []

    for i in range(0, len(position)):
        pairs[position[i]] = speed[i]

    # create keys array
    pos = []
    for key, value in pairs.items():
        pos.append(key)

    sorted_pos = sorted(pos, reverse=True)  # reverse sorted order

    for item in sorted_pos:
        if not stack:
            stack.append(item)
        if stack:
            ahead_pos = stack[-1]
            ahead_speed = pairs[ahead_pos]
            ahead_dist = target - ahead_pos
            ahead_time = ahead_dist / ahead_speed

            behind_pos = item
            behind_speed = pairs[behind_pos]
            behind_dist = target - behind_pos
            behind_time = behind_dist / behind_speed
            # if it takes longer then it does not catch the fleet ahead
            if behind_time > ahead_time:
                stack.append(item)

    fleets = len(stack)

    return fleets
