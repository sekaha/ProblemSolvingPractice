# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type node: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        def match(a,b):
            # both None so they match
            if not a and not b:
                return True
            # 
            if not a or not b:
                return False

            return a.val == b.val and match(a.left,b.left) and match(a.right,b.right)

        if not root:
            return False
        
        if match(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)