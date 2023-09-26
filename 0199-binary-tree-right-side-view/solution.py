class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        self.view = []
        self.traverse(root)

        return [i[-1] for i in self.view]
    
    def traverse(self, root, depth=0):
        if len(self.view) > depth: self.view[depth].append(root.val)
        else: self.view.append([root.val])
        if root.left: self.traverse(root.left, depth + 1)
        if root.right: self.traverse(root.right, depth + 1)
