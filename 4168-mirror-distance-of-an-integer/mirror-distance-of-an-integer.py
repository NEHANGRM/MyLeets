class Solution(object):
    def reverse(self,n):
        rev=0
        while(n>0):
            rev=rev*10+(n%10)
            n//=10
        return rev
    def mirrorDistance(self, n):
        t=n
        return abs(t-self.reverse(t))
        