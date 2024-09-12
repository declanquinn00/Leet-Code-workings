# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recursiveTreeLoop(self, root: Optional[TreeNode], out):
            # value
            out.append(root.val)
            # check left
            if root.left!=None:
                self.recursiveTreeLoop(root.left, out)

            # check right
            if root.right!=None:
                self.recursiveTreeLoop(root.right, out)

            # return
            return out

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            out = []
            if root == None:
                return []
            else:
                out = self.recursiveTreeLoop(root, out)
                return out


    def recursiveTreeLoopP(self, root: Optional[TreeNode], out):
        # check left
        if root.left!=None:
            self.recursiveTreeLoopP(root.left, out)

        # check right
        if root.right!=None:
            self.recursiveTreeLoopP(root.right, out)

        # value
        out.append(root.val)

        # return
        return out

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        if root == None:
            return []
        else:
            out = self.recursiveTreeLoopP(root, out)
            return out