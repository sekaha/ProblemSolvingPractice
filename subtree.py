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
        
        def match(node,sub):
            if sub:
                if node:
                    # if the val's of sub tree and main tree nodes are the same, advance to the next to see if this pattern continues down to the None nodes
                    if node.val == sub.val:
                        return match(node.left,sub.left) and match(node.right,sub.right)
                    # they are not the same, so keep searching from the ORIGINAL subroot
                    else:
                        return match(node.left,subRoot) or match(node.right,subRoot)
                else:
                    # the main tree terminated without finding all the pairs
                    return False
            else:
                # the sub tree terminated, but there might be one more node in the main tree that disqualifies the sub tree
                if node: # if there's another node, keep searching for subtree
                    return match(node,subRoot)
                else:
                    return True
        
        return match(root,subRoot)