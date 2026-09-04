class Solution(object):
    def longestSubarray(self, nums):
        l=0
        c=0
        mx=0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1
            while c>1:
                if nums[l]==0:
                    c-=1
                l+=1
            mx=max(mx,i-l)
        return mx
