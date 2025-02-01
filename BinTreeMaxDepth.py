class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        countleft = 0
        countright = 0
        if not root.left and not root.right:
            return 1

        # search left and right
        if root.left:
            countleft = self.maxDepth(root.left)
        if root.right:
            countright = self.maxDepth(root.right)

        # take max left or right
        count = max(countright, countleft) + 1

        return count