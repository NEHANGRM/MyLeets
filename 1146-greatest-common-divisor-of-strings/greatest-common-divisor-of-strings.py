class Solution(object):
    def gcd(self,m,n):
        while(n!=0):
            m,n=n,m%n
        return m
    def gcdOfStrings(self, str1, str2):
        if str1+str2!=str2+str1:
            return ""
        m=self.gcd(len(str1),len(str2))
        return str1[:m]