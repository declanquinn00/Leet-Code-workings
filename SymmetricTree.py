# Imagine being given a tree (._. )
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def Mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and Mirror(left.left, right.right) and Mirror(left.right, right.left)

        return Mirror(root.left, root.right)
