class Solution(object):
    def gcd(self,a,b):
        while b!=0:
            a,b=b,a%b
        return a
    def lcm(self,a,b):
        return (a*b)//self.gcd(a,b)
    def subarrayLCM(self, nums, k):
        c=0
        for i in range(len(nums)):
            l=nums[i]
            for j in range(i,len(nums)):
                l=self.lcm(l,nums[j])
                if l==k:
                    c+=1
                if l>k:
                    break
        return c
        
        