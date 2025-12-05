# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEqual(self, a, b):
        if not a and not b:
            return True
        elif not a or not b:
            return False

        # check left
        l = self.isEqual(a.left, b.left)
        # check right
        r = self.isEqual(a.right, b.right)
        # check equal
        if a.val == b.val:
            if l and r:
                return True
            else:
                return False
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False
        if not subRoot:
            return True
        # check if equal to current node
        if self.isEqual(root, subRoot):
            return True

        res_l = self.isSubtree(root.left, subRoot)
        res_r = self.isSubtree(root.right, subRoot)
        return res_l or res_r
