class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        if root:
            lst += self.inorderTraversal(root.left)
            lst.append(root.val)
            lst += (self.inorderTraversal(root.right))
        return lst