# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanceCheck(root):
            value = 0
            if root == None:
                return value
            else:
                # check left
                value_left= balanceCheck(root.left)

                # check right
                value_right= balanceCheck(root.right)

                # check if imBalance found
                if value_left == -1 or value_right == -1:
                    return -1

                # compare
                abs_val = abs(value_left - value_right)
                # return if imbalanced is (true anything else) or (false = -1)
                if abs_val > 1:
                    return -1
                else:
                    return max(value_left,value_right) + 1

        if root == []:
            return True
        else:
            val = balanceCheck(root)
            if val == -1:
                return False
            else:
                return True