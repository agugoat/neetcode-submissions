# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            if i == level_size - 1:
                res.append(node.val)
        
        return res



        '''
        input: root of a binary tree
        output: list of the nodes that are visiable by the right side

        examples:
          1 
         /  \
        2     3       <- 👁️     
       / \   /  \
       4  5  6   7
       result = [1,3,7] 

       edge cases?:
       empty root? - > return empty list
       nothing on the right? - > return only the root


       potienal soultions :
       using bfs - > o(n) this seeems quicker going level by level
       using dfs - > o(n)

       pesudo code:

       if the root is none -> return an empty list

       using a queue/ bfs get each level of the tree in an array

       append the last element of the list to res , and keep traversing

        '''
        