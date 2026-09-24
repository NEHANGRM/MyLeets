class Solution(object):
    def sod(self,n):
        s=0
        while(n>0):
            s+=n%10
            n/=10
        return s

    def smallestIndex(self, nums):
        for i,n in enumerate(nums):
            if i==self.sod(n):
                return i
        return -1
        