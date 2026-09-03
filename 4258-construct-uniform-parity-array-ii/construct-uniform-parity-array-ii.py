class Solution(object):
    def uniformArray(self, nums1):
        mn=nums1[0]
        hasodd=False
        for i in nums1:
            if mn>i:
                mn=i
            if i & 1 :
                hasodd=True
        if mn & 1:
            return True
        return not hasodd
        