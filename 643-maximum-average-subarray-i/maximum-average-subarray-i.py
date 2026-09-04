class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        s=0
        for i in range(k):
            s+=nums[i]
        mx=s
        for i in range(k,n):
            s=s+nums[i]-nums[i-k]
            if s>mx:
                mx=s
        return mx/k
        
        