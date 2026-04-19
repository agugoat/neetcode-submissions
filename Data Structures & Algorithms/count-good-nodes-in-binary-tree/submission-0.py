# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodHelp(root,root.val)
    
    

    # recrusion
    def goodHelp(self,root: TreeNode, maxSeen:int) -> int:
        if root == None:
            return 0

        isGood = 0
        if root.val >= maxSeen:
            isGood = 1
        
        maxSeenY = max(maxSeen, root.val)


        left_count = self.goodHelp(root.left,maxSeenY)

        right_count = self.goodHelp(root.right,maxSeenY)

        return isGood + left_count + right_count


            # concepitalulty I know we good
        
        