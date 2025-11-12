def trap(height) -> int:
    l, r = 1, len(height) - 2

    max_l = height[0]
    max_r = height[len(height) - 1]

    total_water = 0

    while l <= r:
        if max_l <= max_r:
            if height[l] <= max_l:
                total_water += max_l - height[l]
            else:
                max_l = height[l]
            l += 1
        else:
            if height[r] <= max_r:
                total_water += max_r - height[r]
            else:
                max_r = height[r]
            r -= 1

    return total_water

height = [0,2,0,3,1,0,1,3,2,1]
print(trap(height))