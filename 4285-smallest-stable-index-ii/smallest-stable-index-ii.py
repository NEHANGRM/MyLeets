class Solution(object):
    def firstStableIndex(self, nums, k):
        n=len(nums)
        mnv=[float('inf')]*(n-1)+[nums[-1]]
        for i in range(n-2,-1,-1):
            mnv[i]=min(mnv[i+1],nums[i])
        mxv=0
        for i in range(n):
            mxv=max(mxv,nums[i])
            if mxv-mnv[i]<=k:
                return i 
        return -1
        