public class Solution {
    public int countDigitOne(int n) {
        if (n < 10) {
            if (n >= 1) return 1;
            else return 0;
        }
        else {
            if (n % 10 == 0) {
                return 10 * countDigitOne(n / 10) - (9 - n % 10) * countOnesNum(n / 10) + n / 10;
            }
            else {
                return 10 * countDigitOne(n / 10) - (9 - n % 10) * countOnesNum(n / 10) + n / 10 + 1;
            }
        }
    }
    
    public int countOnesNum(int num) {
        int count = 0;
        while(num != 0) {
            int d = num % 10;
            if (d == 1) count ++;
            num = num / 10;
        }
        return count;
    }
}
