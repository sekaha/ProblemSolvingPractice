# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        good_nodes = 0

        while stack:
            node, biggest = stack.pop()

            if node.val >= biggest:
                good_nodes += 1
                biggest = node.val
            
            if node.left:
                stack.append((node.left,biggest))

            if node.right:
                stack.append((node.right,biggest))

        return good_nodes

sol = Solution()