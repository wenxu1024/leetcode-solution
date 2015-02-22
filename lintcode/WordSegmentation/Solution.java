import java.util.*;
//word segmentation, dynamic programming

public class Solution {
    /**
     * @param s: A string s
     * @param dict: A dictionary of words dict
     */
    public boolean wordSegmentation(String s, Set<String> dict) {
        // write your code here 
        int l = s.length();
        boolean[] B = new boolean[l + 1];
        int[] chars = new int[256];
        int i, k;
        String str = "";
        Iterator<String> iter = dict.iterator();
        while(iter.hasNext()) {
            str = iter.next();
            int len = str.length();
            for (i = 0; i < len; i ++) {
                chars[str.charAt(i)] ++;
            }
        }
        for (i = 0; i < l; i ++) {
            if (chars[s.charAt(i)] == 0) return false;
        }
        B[0] = true;
        for (i = 1; i < l + 1 ; i ++) {
            str = "";
            B[i] = false;
            for (k = i - 1; k > -1; k --) {
                str = s.charAt(k) + str;
                if (dict.contains(str)) B[i] = B[i] || B[k];
                if (B[i]) break;
            }
        }
        return B[l];
    }
}


