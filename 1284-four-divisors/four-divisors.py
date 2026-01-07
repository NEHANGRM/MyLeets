class Solution(object):
    def sumFourDivisors(self, nums):
        res=0
       
        for i in nums:
            l=set()
            for j in range(1,int(math.sqrt(i))+1):
                if(i%j==0):
                    l.add(j)
                    l.add(i//j)
            if(len(l)==4):
                for k in l:
                    res+=k
        return res

        
        