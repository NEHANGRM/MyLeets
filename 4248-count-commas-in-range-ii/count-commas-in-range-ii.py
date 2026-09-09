class Solution(object):
    def countCommas(self, n):
        p=1000
        r=0
        while p<=n:
            r+=n-p+1 
            p*=1000
        return r


