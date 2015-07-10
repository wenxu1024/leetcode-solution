import java.util.*;

public class Solution {
    public String shortestPalindrome(String s) {
        int l = s.length();
        if (l == 1) return s;
        int lmin = 9999;
        int imin = 9999;
        int k = 0;
        for(int i = 0; i < l / 2; i ++) {
            for(k = 0; k < i; k ++) {
                if(s.charAt(k) != s.charAt(2 * i - k)) break;
            }
            if(k == i) {
                if(2 * l - 2 * i - 1 < lmin) {
                    lmin = 2 * l - 2 * i - 1;
                    imin = i;
                }
            }
        }
	System.out.println(imin);
        String res = "";
        for(int i = l - 1; i > 2 * imin; i --) {
            res += s.charAt(i);
        }
        res += s;
        return res;
   } 

    public static void main(String[] args) {
//	String s = "aacecaaa";
	String s = "abcd";
	Solution sol = new Solution();
	System.out.println(sol.shortestPalindrome(s));
    }
}
