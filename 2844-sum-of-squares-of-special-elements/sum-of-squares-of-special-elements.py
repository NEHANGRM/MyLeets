class Solution(object):
    def sumOfSquares(self, nums):
        s=0
        n=len(nums)
        for i in range(1,len(nums)+1):
            if n%i==0:
                s+=nums[i-1]*nums[i-1]
        return s