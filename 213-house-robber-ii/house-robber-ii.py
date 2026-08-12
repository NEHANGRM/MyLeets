class Solution(object):
    def rob(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        c1=self.comp(nums[1:])
        c2=self.comp(nums[:-1])
        return max(c1,c2)
    def comp(self,nums):
        n=len(nums)
        cur=0
        prev1=0
        prev2=0
        for i in range(len(nums)):
            cur=max(prev2+nums[i],prev1)
            prev2=prev1
            prev1=cur
        return cur
