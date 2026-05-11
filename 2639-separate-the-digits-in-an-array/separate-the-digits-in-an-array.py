class Solution(object):
    def separateDigits(self, nums):
        res=[]
        for i in nums:
            r=0
            f=[]
            while(i>0):
                r=i%10
                f.append(r)
                i//=10
            res.extend(f[::-1])
        return res