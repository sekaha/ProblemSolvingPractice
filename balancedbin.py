from math import ceil

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        stack = [(root,0.0)]
        prev_depth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                stack += (node.left,depth+1),(node.right,depth+1)
                
                print(prev_depth,depth)
                
                prev_depth = depth

        return True