class Solution(object):
    def reverseDegree(self, s):
        a=0
        for i,ch in enumerate(s,start=1):
            a+=(26-(ord(ch)-ord('a')))*i
        return a
