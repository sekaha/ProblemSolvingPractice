# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        right_side = []
        frontier = [root]

        while frontier:
            right_side.append(frontier[-1].val)
            new_frontier = []

            for node in frontier:
                if node.left:
                    new_frontier.append(node.left)

                if node.right:
                    new_frontier.append(node.right)

            frontier = new_frontier

        return right_side
