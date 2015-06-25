import java.util.*;

public class Solution {
/*    public int countPrimes(int n) {
        HashMap<Integer, Boolean> m = new HashMap<Integer, Boolean> ();
        //sieve method
        for(int i = 2; i < n; i ++) m.put(i, true);
        for(int i = 2; i < n; i ++) {
            if (m.get(i) == true) {
                for(int k = 2; k <= n / i; k ++) {
                    if (k * i < n) m.put(k * i, false);
                }
            }
        }
        int res = 0;
        for (int i = 2; i < n; i ++) {
            if (m.get(i) == true) res++;
        }
        return res;
    } */
    
    public int countPrimes(int n) {
        HashMap<Integer, Boolean> m = new HashMap<Integer, Boolean> ();
        //sieve method
        for(int i = 2; i < n ; i ++) m.put(i, true);
        for(int i = 2; i < Math.sqrt(n) ; i ++) {
            if (m.get(i) == true) {
                for(int k = 0; i * i + i * k < n; k ++) {
                    m.put(i * i + k * i, false);
                }
            }
        }
        int res = 0;
        for(int i = 2; i < n; i ++) {
            if (m.get(i) == true) res ++;
        }
        return res;
    }

    public static void main(String[] args) {
	int n = 999983;
	Solution s = new Solution();
	System.out.println(s.countPrimes(n));
    }
}
