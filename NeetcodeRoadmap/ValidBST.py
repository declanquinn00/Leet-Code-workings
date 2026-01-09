class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lo, hi):
            if node.left:
                if node.left.val < node.val and lo < node.left.val and node.left.val < hi:
                    if not dfs(node.left, lo, node.val):
                        return False
                else:
                    return False
            if node.right:
                if node.right.val > node.val and lo < node.right.val and node.right.val < hi:
                    if not dfs(node.right, node.val, hi):
                        return False
                else:
                    return False

            return True

        res = dfs(root, float('-inf'), float('inf'))
        return res