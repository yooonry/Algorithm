class Solution {
    boolean solution(String s) {
        String sLower=s.toLowerCase();
        int p=0, y=0;

        for (int i=0; i<s.length(); i++) {
            if (sLower.charAt(i)=='p')
                p++;
            
            else if (sLower.charAt(i)=='y')
                y++;
        }
        
        if (p==y)
            return true;
        
        else
            return false;
    }
}
