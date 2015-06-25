public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int n = nums.length;
        Map<Integer, Integer> m = new HashMap<Integer, Integer> ();
        for(int i = 0; i < n; i ++) {
            if (m.containsKey(nums[i])) {
                int index = m.get(nums[i]);
                if (i - index <= k) return true;
                else m.put(nums[i], i);
            }
            else {
                m.put(nums[i], i);
            }
        }
        return false;
    }
}
