class Solution 
{
    public String convert(String s, int n) 
    {
        String res="";
        int count[]=new int[n];
        char a[][]=new char[n][s.length()];

        for(int i=0;i<n;i++)
            count[i]=0;
        int pos=0;
        while(true)
        {
            for(int i=0;i<=n-1 && pos<s.length();i++)
            {
                a[i][count[i]]=s.charAt(pos);
                pos=pos+1;
                count[i]++;
            }
            for(int i=n-2;i>=1 && pos<s.length();i--)
            {
                a[i][count[i]]=s.charAt(pos);
                pos++;
                count[i]++;
            }
            if(pos>=s.length())
                break;
        }
        for(int i=0;i<n;i++)
            for(int j=0;j<count[i];j++)
                res=res+a[i][j];
        return res;
    }
}