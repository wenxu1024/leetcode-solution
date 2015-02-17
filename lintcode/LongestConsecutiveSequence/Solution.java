import java.util.*;

// Longest consecutive sequence

public class Solution {
    /**
     * @param nums: A list of integers
     * @return an integer
     */
    public int longestConsecutive(int[] num) {
        // write you code here
        Set<Integer> s = new HashSet<Integer> ();
        int i, next, prev, l = num.length;
        for (i = 0; i < l; i ++) {
            s.add(num[i]); //atuoboxing
        }
        int count, maxcount = 0;
        for (i = 0; i < l; i ++) {
            if (s.contains(num[i])) {
                next = num[i] - 1;
                count = 1;
                s.remove(num[i]);
                while (s.contains(next)) {
                    count ++;
                    s.remove(next);
                    next --;
                }
                prev = num[i] + 1;
                while (s.contains(prev)) {
                    count ++;
                    s.remove(prev);
                    prev ++;
                }
                maxcount = Math.max(maxcount, count);
            }
        }
        return maxcount;
    }
}


