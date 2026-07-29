class Solution(object):
    def check(self, nums):
        if len(nums)<=1:
            return True
        ic=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                ic+=1
                if ic>1:
                    return False
        if nums[0]<nums[len(nums)-1]:
            ic+=1

        return ic<=1
        