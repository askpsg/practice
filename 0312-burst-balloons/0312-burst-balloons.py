class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        for interval in range(2, n):
            for i in range(0, n - interval):
                j = i + interval
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + nums[i]*nums[k]*nums[j] + dp[k][j])
        
        return dp[0][n-1]