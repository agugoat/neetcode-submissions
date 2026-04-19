class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        dp = (amount +1) * [float('inf')]

        dp[0] = 0


        for i in range(1,amount+1):
            for coin in coins:
                
                if i - coin >= 0:
                    dp[i] = min(dp[i-coin] + 1, dp[i])
        
        return -1 if dp[amount] == float('inf') else dp[amount]



        '''
        input: amount , list of coins  
        output: the miniumn amount of coins to reach amount -> int

        example:
        coins = [1,5,10], amount = 12
        10 + 1 + 1 = 3
        coins = [2], amount = 3
        we cant reach it , 2 + 2 = 4

        edge cases:
        what if we have no coins - > return -1
        what if we cant reach the number of coins -> return -1
        what if we have no amount - > return 0

        potienal solutions:
        use a dynamic programming apporach ->
        what would dp[i] , dp[0] is atleast 1 coin
        dp[i] reps the minminm coins for that amount

        pesudo -code


        '''
        