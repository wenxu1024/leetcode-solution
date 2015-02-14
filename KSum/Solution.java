import java.util.*;
public class Solution {
    /**
     * @param A: an integer array.
     * @param k: a positive integer (k <= length(A))
     * @param target: a integer
     * @return an integer
     */
    public int  kSum(int A[], int k, int target) {
        // write your code here
        int i, j, s, l;
        l = A.length;
        Arrays.sort(A);
        int[][][] N = new int[l + 1][k + 1][target + 1];
        
        for (j = 0; j < k + 1; j ++) {
            for(i = 0; i < l + 1; i ++) {
                for(s = 0; s < target + 1; s ++) {
                    if (i < j) N[i][j][s] = 0;
                    else {
                        if (j == 0) N[i][j][0] = 1;
                        else N[i][j][0] = 0;
                    }
                }
            }
        }
        
        for (j = 1; j < k + 1; j ++) {
            for (i = j; i < l + 1; i ++) {
                for(s = 0; s < target + 1; s++) {
                    if (A[i - 1] > s) {
                        N[i][j][s] = N[i - 1][j][s];
                    }
                    else {
                        N[i][j][s] = N[i - 1][j][s] + N[i - 1][j - 1][s - A[i - 1]];
                    }
                }
            }
        }
        return N[l][k][target];
    }


    public static void main(String[] args) {
	int[] A = {1, 2, 3, 4};
        int k = 2;
        int target = 5;
        Solution sol = new Solution();
        System.out.println("The answer for " + Arrays.toString(A) + " with k = " + k + " and target = " + target + " is: " + sol.kSum(A, k, target));
	}
}



