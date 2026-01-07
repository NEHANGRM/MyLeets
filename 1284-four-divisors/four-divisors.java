class Solution {
    public int sumFourDivisors(int[] nums) {
        int sum=0;
        for(int i:nums)
        {
            Set<Integer> l=new HashSet <Integer>();
            for(int j=1;j<=Math.sqrt(i);j++)
            {
                if(i%j==0){
                l.add(j);
                l.add((int)i/j);
                }
            }
            if(l.size()==4)
            for(int k:l)
            sum+=k;
        }
        return sum;
    }
}