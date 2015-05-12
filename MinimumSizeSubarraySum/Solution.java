public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
/*        int l = nums.length;
        int[][] sum = new int[l][l + 1];
        int i, j;
        for(i = 0; i < l; i ++) sum[i][0] = 0;
        for(j = 1; j < l + 1; j ++) {
            for(i = 0; i < l - j + 1; i ++) {
                sum[i][j] = sum[i][j - 1] + nums[i + j - 1];
                if (sum[i][j] >= s) return j;
            }
        }
        return 0;*/
        
        int l = nums.length;
        int i, j, k;
        int[] sum = new int[l + 1];
        int accumulate = 0;
        sum[0] = 0;
        for(i = 0; i < l; i ++) {
            accumulate += nums[i];
            sum[i + 1] = accumulate;
        }
        i = 0;
        j = 1;
        k = 99999;
        if (l == 0) return 0;
        while(j < l + 1) {
            while(j < l + 1 && sum[j] - sum[i] < s) j ++;
            if (j == l + 1 && i == 0) return 0;
            if (j < l + 1) {
                k = Math.min(j - i, k);
                while(sum[j] - sum[i] >= s) {
                    k = Math.min(j - i, k);
                    i ++;
                }
            }
        }
        return k;
    }
}
