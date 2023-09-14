class Solution:
    def depth(self, p, d):
        if not p: return d
        return max(self.depth(p.left, d + 1), self.depth(p.right, d + 1))
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root, 0)
