class Solution(object):
    def findMaxAverage(self, nums, k):
        n=len(nums)
        s=0
        for i in range(k):
            s+=nums[i]
        mx=s
        for i in range(k,n):
            s=s+nums[i]-nums[i-k]
            if s>mx:
                mx=s
        return float(mx)/k
        