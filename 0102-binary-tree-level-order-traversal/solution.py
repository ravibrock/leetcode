class Solution:
    def __init__(self):
        self.ls = []
        self.fin = []
    
    def traverse(self, root, level):
        if root.left:
            self.ls.append((root.left.val, level))
            self.traverse(root.left, level + 1)
        if root.right:
            self.ls.append((root.right.val, level))
            self.traverse(root.right, level + 1)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return self.fin

        self.fin.append([root.val])
        self.traverse(root, 1)
        for i in self.ls:
            if len(self.fin) > i[1]: self.fin[i[1]].append(i[0])
            else: self.fin.append([i[0]])

        return self.fin
