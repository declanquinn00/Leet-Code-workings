# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def getMin(root):
            val = 0
            # check if null
            if root == None:
                return val
            # check left
            val_left = getMin(root.left)
            # check right
            val_right = getMin(root.right)

            if val_left == 0:
                min_val = val_right
            elif val_right == 0:
                min_val = val_left
            else:
                # get the minimum search tree length
                min_val = min(val_left, val_right)
                # return the lowest value
            return min_val + 1

        if root == None:
            return 0
        else:
            return getMin(root)