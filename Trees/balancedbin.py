# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        stack = [(root, False)]
        depths = {}

        while stack:
            node, visited = stack.pop()

            if node:
                if visited:
                    l_d = depths.get(node.left,0)
                    r_d = depths.get(node.right,0) 
                    depths[node] = max(l_d,r_d)+1

                    if abs(l_d - r_d) > 1:
                        return False
                else:
                    stack.append((node,True))
                    stack.append((node.left,False))
                    stack.append((node.right ,False))
            else:
                depths[node] = 0

        return True