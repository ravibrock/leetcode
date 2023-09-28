class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: return self.DFS(root)[k - 1]
    def DFS(self, r, v=[]): return self.DFS(r.left, v) + [r.val] + self.DFS(r.right, v) if r else v
