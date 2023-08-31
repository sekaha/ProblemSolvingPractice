# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        def get_depth_and_diameter(node):
            l_dep, r_dep, l_dia, r_dia = 0, 0, 0, 0

            if node.left:
                l_dep, l_dia = get_depth_and_diameter(node.left)
            
            if node.right:
                r_dep, r_dia = get_depth_and_diameter(node.right)

            dep = max(l_dep,r_dep)+1
            dia = max(r_dep+l_dep, r_dia, l_dia)
            
            return dep, dia

        return get_depth_and_diameter(root)[1]