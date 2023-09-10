class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = 0

        def visit(node):
            ret = -1

            if node.left:
                ret = visit(node.left)

            nonlocal visited
            visited += 1

            if visited == k:
                return node.val

            if node.right:
                ret = max(ret,visit(node.right))

            return ret

        return v