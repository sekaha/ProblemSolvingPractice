from math import ceil

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def dfs(node):
            if node:
                l_d, l_b = dfs(node.left)
                r_d, r_b = dfs(node.right)

                depth = max(l_d,r_d)
                balanced = (l_b and r_b) and (abs(l_d-r_d) <= 1)

                return depth+1, balanced
            else:
                return 0, True

        return dfs(root)[1]