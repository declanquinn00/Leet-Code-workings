# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def isEqual(Treea, Treeb):
    if not Treea and not Treeb:
        return True
    if Treea and Treeb and Treea.val == Treeb.val:
        return (isEqual(Treea.left,Treeb.left) and isEqual(Treea.right,Treeb.right))
    else:
        return False