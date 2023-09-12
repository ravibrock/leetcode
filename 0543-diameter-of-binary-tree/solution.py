class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calcHeight(root, depth):
            if not root: return depth
            
            return max(
                calcHeight(root.left, depth + 1),
                calcHeight(root.right, depth + 1)
            )
        
        def calcDiameter(root, diameter):
            if not root: return diameter

            diameter = max(
                diameter,
                calcHeight(root.left, 0) + calcHeight(root.right, 0)
            )
            return max(
                calcDiameter(root.left, diameter),
                calcDiameter(root.right, diameter)
            )
        
        return calcDiameter(root, 0)
