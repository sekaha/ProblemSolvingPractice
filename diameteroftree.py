# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        def get_depth_and_diameter(node):
            l_dep, l_dia, r_dep, r_dia = -1, -1, -1, -1

            if node.left:
                l_dep, l_dia = get_depth_and_diameter(node.left)

            if node.right:
                r_dep, r_dia = get_depth_and_diameter(node.right)
            
            pot_dia = (l_dep+1) + (r_dep+1)

            return max(r_dep,l_dep)+1, max(l_dia+1,r_dia+1,pot_dia)
            
        return get_depth_and_diameter(root)[0]