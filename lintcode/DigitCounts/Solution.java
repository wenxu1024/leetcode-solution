import java.util.*;
//Digit Counts

class Solution {
    /*
     * param k : As description.
     * param n : As description.
     * return: An integer denote the count of digit k in 1..n
     */
    public int digitCounts(int k, int n) {
        // write your code here
        if (n >= 0 && n <=9) {
            if (k <= n) return 1;
            else return 0;
        }
        int c, i, n1, n2;
        c = n;
        i = 1;
        while (c > 9) {
            c /= 10;
            i *= 10;
        }
        n1 = n / i; // convert to subproblem 0[0 .. i - 1] , 1[0 .. i - 1], ...
        n2 = n % i;
        if (n1 == k) {
            return k * digitCounts(k, i - 1) + (n2 + 1) + digitCounts(k, n2); // build from subproblem
        } //according to three scenarios
        else if (n1 < k) {
            return n1 * digitCounts(k, i - 1) + digitCounts(k, n2);
        }
        else {
            return n1 * digitCounts(k, i - 1) + i + digitCounts(k, n2);
        }
        
    }


    public static void main(String[] args) {
	int k = 1;
	int n = 1222222;
	Solution sol = new Solution();
	System.out.println("the answer for k = " + k + " n = " + n + " is: " + sol.digitCounts(k, n));
    }
};



