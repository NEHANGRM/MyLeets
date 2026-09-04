class Solution(object):
    def maxVowels(self, s, k):
        vowel='AEIOUaeiou'
        c=0
        for i in range(k):
            if s[i] in vowel:
                c+=1
        mx=c
        for i in range(k,len(s)):
            if s[i-k] in vowel:
                c-=1
            if s[i] in vowel:
                c+=1
            mx=max(mx,c)
        return mx