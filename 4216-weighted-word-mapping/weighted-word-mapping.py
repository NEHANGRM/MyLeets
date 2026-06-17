class Solution(object):
    def mapWordWeights(self, words, weights):
        res=[]
        for i in words:
            s=0
            for c in i:
                s+=weights[(ord(c)-ord("a"))]
            res.append(chr(ord("z")-s%26))
        return "".join(res)
        