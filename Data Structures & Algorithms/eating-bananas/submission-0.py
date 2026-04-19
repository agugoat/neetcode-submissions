class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        min_speed = right
        left = 1


        while left <= right:
            mid = left + (right-left) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil((p) / mid)
            if totalTime <= h:
                min_speed = mid
                right = mid - 1
            else:
                left = mid +1
        
        return min_speed




