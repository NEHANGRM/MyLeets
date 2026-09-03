class Solution(object):
    def minCostClimbingStairs(self, cost):
        n=len(cost)
        dp=[0]*n
        for i in range(len(cost)):
            if i<2:
                dp[i]=cost[i]
            else:
                dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[n-1],dp[n-2])