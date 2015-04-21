public class Solution {
    public int rob(int[] num) {
        int l = num.length;
        if (l == 0) return 0;
        int i;
        int[] money = new int[l + 1];
        money[0] = 0;
        money[1] = num[0];
        for(i = 2; i <= l; i ++) {
            money[i] = Math.max(money[i - 1], money[i - 2] + num[i - 1]);
        }
        return money[l];
    }
}
