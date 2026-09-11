class Solution(object):
    def totalNumbers(self, digits):
        n=len(digits)
        v=[False]*1000
        res=ans=0
        for i in range(n):
            if digits[i]==0:
                continue
            for j in range(n):
                if i==j:
                    continue
                for k in range(n):
                    if i==k or j==k or digits[k]%2!=0:
                        continue
                    res=100*digits[k]+10*digits[j]+digits[i]
                    if not v[res]:
                        v[res]=True
                        ans+=1
        return ans
        