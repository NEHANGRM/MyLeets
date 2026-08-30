class Solution(object):
    def countSpecialIntegers(self, nums):
        freq=Counter(nums)
        first={}
        last={}
        for i in range(len(nums)):
            if nums[i] not in first:
                first[nums[i]]=i
            last[nums[i]]=i
        c=0
        for i in freq:
            if last[i]-first[i]+1==freq[i]:
                c+=1

        return c

        