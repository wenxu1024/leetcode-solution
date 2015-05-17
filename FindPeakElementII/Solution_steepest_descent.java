import java.util.*;

class Solution {
    /**
     * @param A: An integer matrix
     * @return: The index of the peak
     */
    public List<Integer> findPeakII(int[][] A) {
        // write your code here
        //steepest descent algorithm, -A(x,y) is the cost function
        //try to minimize -A
        List<Integer> res = new ArrayList<Integer> ();
        int x = 1;
        int y = 3;
        while(A[x][y] <= A[x + 1][y] || A[x][y] <= A[x - 1][y] || A[x][y] <= A[x][y - 1] || A[x][y] <= A[x][y + 1]) {
            if (A[x + 1][y] - A[x][y] > 0 && A[x][y + 1] - A[x][y] > 0) {
                x = x + 1;
 	        y = y + 1;
            }
	    else if (A[x + 1][y] - A[x][y] > 0 && A[x][y + 1] - A[x][y] <= 0) {
		x = x + 1;
		//y = y - 1;
		y = y;
	    }
	    else if (A[x + 1][y] - A[x][y] <= 0 && A[x][y + 1] - A[x][y] > 0) {
		x = x - 1;
		y = y + 1;
    	    }
	    else {
		x = x - 1;
		y = y - 1;
	    }	
	    if (x >= A.length) x = x - 1;
	    if (x <= 0) x = x + 1;
	    if (y >= A[0].length) y = y - 1;
	    if (y <= 0) y = y + 1;
	    System.out.print(x);
	    System.out.print(',');
	    System.out.println(y);
        }
        res.add(x);
        res.add(y);
        return res;
    }

    public static void main(String[] args) {
//	int[][] A = {{1,2,3,4,5,6},{14,15,16,17,18,8},{12,13,11,10,9,7}};
	int[][] A = {{1,2,3,6,5},{16,41,23,22,6},{15,17,24,21,7},{14,18,19,20,10},{13,14,11,10,9}};
	Solution sol = new Solution();
	System.out.println(sol.findPeakII(A));
    }
}



