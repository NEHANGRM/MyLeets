class Solution {
    public boolean isTrionic(int[] nums) {
        int p=0,q=0,i=1,f=0;
        while(i<nums.length && nums[i-1]<nums[i])
            i++;
        p=i-1;
        while(i<nums.length && nums[i-1]>nums[i])
            i++;
        q=i-1;
        while(i<nums.length && nums[i-1]<nums[i])
            i++;
        f=i-1;
        
        return (p!=0 && q!=p && (f!=q && f==nums.length-1));
    }
}