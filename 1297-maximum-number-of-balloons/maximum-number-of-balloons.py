class Solution(object):
    def maxNumberOfBalloons(self, text):
        b=a=l=o=n=0
        for i in text:
            if i=='b': b+=1
            if i=='a': a+=1
            if i=='l': l+=1
            if i=='o': o+=1
            if i=='n': n+=1
        return min(b,a,l//2,o//2,n)

                

        