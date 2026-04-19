class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        # basically run binary search twice
        # once to get the poteintal range, another to lock in on that range

        left = 0
        right = n-1

        while left <= right:
            center = (left + right) //2 
            if target == matrix[center][0]:
                return True

            elif matrix[center][0] < target:
                left = center + 1
            else:
                right = center-1 
        
        
        start = right  # of the row we need to check

        left = 0
        right = m-1

        # second binary search
        while left <= right:
            center = (left + right) //2 
            if target == matrix[start][center]:
                return True

            elif matrix[start][center] < target:
                left = center + 1
            else:
                right = center-1 
        
        return False


