class Solution(object):
    def letterCombinations(self, digits):
        ans=[]
        if not digits:
            return []
        dl={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def bt(i,c):
            if i==len(digits):
                ans.append(''.join(c))
                return 
            for l in dl[digits[i]]:
                bt(i+1,c+l)

        bt(0,"")
        return ans