class Solution(object):
    def leftRightDifference(self, nums):
        ans=[]
        for i in range(len(nums)):
            ans.append(abs(sum(nums[:i])-sum(nums[i+1:])))
        return ans

        