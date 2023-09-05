# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return TreeNode().left
        def swap(node):
            node2 = TreeNode(val=node.val)
            if node.left: node2.right = swap(node.left)
            if node.right: node2.left = swap(node.right)

            return node2
        
        return swap(root)
