class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.DFS(root)[k - 1]
    
    def DFS(self, root, vals=[]):
        if root:
            return self.DFS(root.left, vals) + [root.val] + self.DFS(root.right, vals)
        else:
            return vals
