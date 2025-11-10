class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def recursion(start,end):
        if start == end:
            return None
        mid = start + end // 2
        root = TreeNode(val=nums[mid], left=recursion(start,mid),Right=recursion(mid+1,end))
        return root

    # calculate binary tree from recursive arg
    return recursion(0, len(nums))

