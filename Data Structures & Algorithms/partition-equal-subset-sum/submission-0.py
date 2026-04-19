class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        total = sum(nums)
        target = total // 2

        if total % 2 == 1:
            return False
       

        dp = [False] * (target+1)

        dp[0] = True

        for k in nums:
            for i in range(target, k-1 , -1):
                dp[i] = dp[i] or dp[i-k]
            
        return dp[target]


        