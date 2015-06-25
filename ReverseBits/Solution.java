import java.util.*;

public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        String s = Integer.toString(n, 2);
	int l = s.length();
	System.out.println(s);
        StringBuffer sb = new StringBuffer(s);
        sb.reverse();
	for (int j = 0; j < 32 - l; j ++) sb.append('0');
        s = new String(sb);
	System.out.println(s);
        return Integer.valueOf(s, 2);
    }
	
    public static void main(String[] args) {
	int n = 0;
	Solution sol = new Solution();
	int k = Integer.parseInt("11111111111111111111111111111111",2);
	System.out.print(sol.reverseBits(n) + k);
    }
}
