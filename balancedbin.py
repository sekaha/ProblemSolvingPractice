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
            layer_dif = [2,0]

            for node in frontier:
                nodes += 1
                dif = 0

                if node.left:
                    dif += 1
                    new_frontier.append(node.left)
                if node.right:
                    dif +=1
                    new_frontier.append(node.right)
                
                layer_dif = [min(layer_dif[0],dif),max(layer_dif[1],dif)]

            frontier = new_frontier

            if layer_dif[1]-layer_dif[0] > 1:
                return False


        return True