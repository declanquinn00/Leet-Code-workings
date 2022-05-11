def isPalindrome(x):
    numbers = []
    for digit in str(x):
        if digit == '-':
            return False
        numbers.append(int(digit))

    i = 0
    j = len(numbers)-1

    while i!=j and i<j:
        if numbers[i] != numbers[j]:
            return False
        i=i+1
        j=j-1
    return True


x = -411234565432114
numbers = isPalindrome(x)
print(numbers)