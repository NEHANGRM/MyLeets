class Solution(object):
    def rob(self, nums):
        n=len(nums)
        dp=[-1]*(n+1)
        return self.solve(nums,n-1,dp)

    def solve(self,nums,i,dp):
        if i<0:
            return 0
        if i==0:
            return nums[0]
        if dp[i]!=-1:
            return dp[i]
        pick=nums[i]+self.solve(nums,i-2,dp)
        notpick=self.solve(nums,i-1,dp)
        dp[i]=max(pick,notpick)
        return dp[i]


