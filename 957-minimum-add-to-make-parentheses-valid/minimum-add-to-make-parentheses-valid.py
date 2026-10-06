class Solution(object):
    def minAddToMakeValid(self, s):
        o,r=0,0
        for i in s:
            if i=='(':
                o+=1
            else:
                if o>0:
                    o-=1
                else:
                    r+=1
        return r+o


        