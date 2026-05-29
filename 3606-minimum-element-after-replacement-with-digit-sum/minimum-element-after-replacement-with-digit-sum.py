class Solution(object):
    def sod(self,n):
        s=0
        while n>0:
            s+=n%10
            n/=10
        return s
    def minElement(self, nums):
        res=[]
        for i in nums:
            res.append(self.sod(i))
        return min(res)