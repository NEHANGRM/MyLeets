class Solution(object):
    def maxOperations(self, nums, k):
        freq=Counter()
        c=0
        for i in nums:
            need=k-i
            if freq[need]>0:
                c+=1
                freq[need]-=1
            else:
                freq[i]+=1
        return c
'''        nums.sort()
        i,j=0,len(nums)-1
        c=0
        while(i<j):
            if nums[i]+nums[j]==k:
                c+=1
                i+=1
                j-=1
            elif nums[i]+nums[j]<k:
                i+=1
            else:
                j-=1
        return c '''