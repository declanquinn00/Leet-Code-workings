class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        ptr1 = 0
        ptr2 = 1
        index = 0
        # get upper bound
        while index < size and numbers[index] < target:
            index = index + 1
        # upperbound is index - 1
        ptr2 = index - 1

        found = False
        while not found:
            added = numbers[ptr1] + numbers[ptr2]
            if added != target:
                if added > target:
                    ptr2 = ptr2 - 1
                elif added < target:
                    ptr1 = ptr1 + 1
            else:
                found = True
                return [min(numbers[ptr1],numbers[ptr2]), max(numbers[ptr1]
                ,numbers[ptr2])]
