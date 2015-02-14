import java.util.*;

public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    public int backPack(int m, int[] A) {
        // write your code here
        int n = A.length;
        int[] Sprev = new int[m + 1]; //Maximum Size we can fill the backpack
        int[] Snext = new int[m + 1];
        int i, j;
        for (j = 0; j < m + 1; j ++) Sprev[j] = 0; //if empty items, the maximum size is 0, (i = 0)
        for (i = 1; i < n + 1; i ++) {
            for (j = 0; j < m + 1; j ++) {
                if (A[i - 1] > j) Snext[j] = Sprev[j];
                else {
                    Snext[j] = Math.max(Sprev[j], Sprev[j - A[i - 1]] + A[i - 1]);
                }
            }
            for (j = 0; j < m + 1; j ++ ) Sprev[j] = Snext[j];
        }
        return Snext[m];
    }

    public static void main(String[] args) {
	int[] A = {2, 3, 5, 7};
        int m = 11;
        Solution sol = new Solution();
        System.out.println("the answer for " + Arrays.toString(A) + " is: " + sol.backPack(m, A));
    }
}


