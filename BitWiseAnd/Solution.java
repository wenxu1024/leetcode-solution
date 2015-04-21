public class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        if (m == 2147483647) return m;
        int res, i;
        if (n == 2147483647) n -= 1;
        if (m > 2147483647 / 2) {
            res = m;
            for (i = m + 1; i <= n; i ++) {
                res = res & i;
            }
            return res;
        }
        int twopower = 1;
        while (twopower < m) {
            twopower <<= 1;
        }
        res = m;
        for (i = m + 1; i <= Math.min(n, twopower - 1); i ++) {
            res = res & i;
        }
        return res;
    }

    public static void main(String[] args) {
	int m = 2147483646;
	int n = 2147483647;
	Solution s = new Solution();
	System.out.println(s.rangeBitwiseAnd(m, n));
    }
}
