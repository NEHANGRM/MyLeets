class Solution(object):
    def digisum(self,n):
        s=0
        while n>0:
            s+=n%10
            n/=10
        return s
    def digiprod(self,n):
        p=1
        while n>0:
            p*=n%10
            n/=10
        return p
    def checkDivisibility(self, n):
        return  True if ((n%(self.digisum(n)+self.digiprod(n)))==0) else False
        