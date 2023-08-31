from math import ceil

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        frontier = [root]
        layers = 0
        nodes = 0

        if root == None:
            return True

        while frontier:
            new_frontier = []

            for node in frontier:
                    nodes += 1

                    if node.left:
                        new_frontier.append(node.left)
                    if node.right:
                        new_frontier.append(node.right)

            frontier = new_frontier
            layers += 1

        print(layers, nodes)
        
        return (layers) == ceil(nodes**0.5)