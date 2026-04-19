# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        
        right = self.maxDepth(root.right) + 1

        left = self.maxDepth(root.left) + 1


        return max(right,left)

        
        
        '''
        input : A binary tree with nodes
        output: an int that represents the max depth

        example inputs: - the max depth would be 3
            1
          /   \              
         2     3
         /\    /\
        4  5  6  7
        
        edge cases:
        what if root is empty
        unblanced tree- no only binary trees are allowed

        potential solutions:

        Do recursive depth first search and keep track of each time u recurse to a 
        new node. Time complexity O(n) , Space(H)

        pesduo code:

        1. check if there is a root, if not return 0 

        2. recurse on every node, track left and right 

        3. return the max height of either left or right

        '''


        