class Solution(object):
    def firstStableIndex(self, nums, k):
        for i in range(len(nums)):
            mx=mn=nums[i]
            for j in range(i):
                mx=max(mx,nums[j])
            for j in range(i+1,len(nums)):
                mn=min(mn,nums[j])
            score=mx-mn
            if score<=k:
                return i
        return -1
        