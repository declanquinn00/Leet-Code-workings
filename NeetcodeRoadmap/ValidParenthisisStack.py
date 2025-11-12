def isValid(self, s: str) -> bool:
    stack = []
    lookup = {'(': ')', '{': '}', '[': ']'}
    inputs = {'(', '{', '['}
    outputs = {')', '}', ']'}

    if s == None:
        return False

    if s[0] not in inputs:
        return False

    for char in s:
        if char in inputs:
            # add to stack
            stack.append(char)

        if char in outputs:
            # pop from stack
            if stack != []:
                top = stack.pop()
            else:
                return False

            if lookup[top] != char:
                return False

    # if stack not empty
    if stack != []:
        return False
    return True