class Solution {
    public String processStr(String s) {
        String res="";
        for(int i=0;i<s.length();i++)
        {
            char ch=s.charAt(i);
            if(ch=='*'){
                if(res!=""){
                     if (res == null || res.isEmpty()) 
                        res="";
                    else
                    res=res.substring(0,res.length()-1);
                }
            }
            else if(ch=='#')
                res+=res;
            else if(ch=='%'){
                String rev=new StringBuilder(res).reverse().toString();
                res=rev;
            }
            else
            res+=ch;

            }
            return res;
        }

    }