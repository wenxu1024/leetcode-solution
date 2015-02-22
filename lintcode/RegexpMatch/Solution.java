// regular expression matching

import java.util.*;

public class Solution {
    /**
     * @param s: A string 
     * @param p: A string includes "." and "*"
     * @return: A boolean
     */
    public boolean isMatch(String s, String p) {
        // write your code here
        int i, j, m, n;
        m = s.length();
        n = p.length();
        boolean[][] B = new boolean[m + 1][n + 1];
        B[0][0] = true;
        for (i = 1; i < m + 1; i ++) B[i][0] = false;
        for (j = 1; j < n + 1; j ++) {
            if (j == 1) {
                B[0][j] = false;
            }
            else {
                if (p.charAt(j - 1) == '*') B[0][j] = B[0][j - 2];
                else B[0][j] = false;
            }
        }

        
        for (i = 1; i < m + 1; i ++) {
            for (j = 1; j < n + 1; j ++) {
                if (j == 1) {
                    if (p.charAt(j - 1) == '.') B[i][j] = B[i - 1][j - 1];
                    else if (p.charAt(j - 1) == s.charAt(i - 1)) B[i][j] = B[i - 1][j - 1];
                    else B[i][j] = false;
                }
                else {
                    if (p.charAt(j - 1) == '.') {
                        B[i][j] = B[i - 1][j - 1];
                    }
                    else if (p.charAt(j - 1) == '*') {
                        if (p.charAt(j - 2) == '.') {
                            B[i][j] = B[i - 1][j] || B[i][j - 2];
                        }
                        else {
                            if (p.charAt(j - 2) != s.charAt(i - 1)) B[i][j] = B[i][j - 2];
                            else B[i][j] = B[i - 1][j] || B[i][j - 2];
                        }
                    }
                    else {
                        if (p.charAt(j - 1) == s.charAt(i - 1)) B[i][j] = B[i - 1][j - 1];
                        else B[i][j] = false;
                    }
                }
            }
        }
        return B[m][n];
        
    }


    public static void main(String[] args) {
	String s = "aasdf";
	String p = "aasdf.*";
	Solution sol = new Solution();
	System.out.println("s: " + s + "   p: " + p + "    " + sol.isMatch(s,p));
    }
    
    
}


