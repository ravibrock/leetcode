class Solution:
    def __init__(self):
        self.ls = []
    
    def traverse(self, root, level):
        if root.left:
            self.ls.append((root.left.val, level))
            self.traverse(root.left, level + 1)
        if root.right:
            self.ls.append((root.right.val, level))
            self.traverse(root.right, level + 1)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        else: self.ls.append((root.val, 0))

        self.traverse(root, 1)

        fin_ls = []
        for i in self.ls:
            if len(fin_ls) > i[1]: fin_ls[i[1]].append(i[0])
            else: fin_ls.append([i[0]])

        return fin_ls
