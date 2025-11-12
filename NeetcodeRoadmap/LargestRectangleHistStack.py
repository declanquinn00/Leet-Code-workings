def largestRectangleArea(heights) -> int:
    maxArea = 0
    stack = []  # pair: (index, height)

    for i, h in enumerate(heights):
        start = i
        # I like this way of doing stacks -> while stack then append
        # while the prev h is less then current h
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            # reset the new start index of that pointer this is where I went wrong!!!
            start = index
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea

heights = [7,1,7,2,2,4]
print(largestRectangleArea(heights))