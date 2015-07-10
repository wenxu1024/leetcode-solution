public class Solution {
    public List<int[]> getSkyline(int[][] buildings) {
        int i = 0;
        int j = buildings.length - 1;
        return getSkylineHelper(buildings, i, j);
    }
    
    
    public List<int[]> getSkylineHelper(int[][] buildings, int i, int j) {
        if(i == j + 1) {
            List<int[]> res = new ArrayList<int[]> ();
            return res;
        }
        else if (i == j) {
            List<int[]> res = new ArrayList<int[]> ();
            int[] x = {buildings[i][0], buildings[i][2]};
            int[] y = {buildings[i][1], 0};
            res.add(x); res.add(y);
            return res;
        }
        else {
            int k = (i + j) / 2;
            //divide problem into two subproblems
            List<int[]> left = getSkylineHelper(buildings, i, k);
            List<int[]> right = getSkylineHelper(buildings, k + 1, j);
            List<int[]> res = new ArrayList<int[]> ();
            //start merging
            int s, t;
            s = 0;
            t = 0;
            int h1, h2, h;
            h1 = 0; h2 = 0;
            int m, n;
            m = left.size();
            n = right.size();
            int l; //record critial points processed.
            l = 0;
            int[] sentinel = {2147483647, 0};
            left.add(sentinel);
            right.add(sentinel);
            while(l <= m + n) {
                if (left.get(s)[0] < right.get(t)[0]) {
                    h1 = left.get(s)[1];
                    h = Math.max(h1, h2);
                    int[] pos = {left.get(s)[0], h};
                    if(res.isEmpty() || res.get(res.size() - 1)[1] != pos[1]) {// skip same level points
                        res.add(pos);
                    }
                    s ++;
                    l ++;
                }
                else if (left.get(s)[0] == right.get(t)[0]) {
                    h1 = left.get(s)[1];
                    h2 = right.get(t)[1];
                    h = Math.max(h1, h2);
                    int[] pos = {left.get(s)[0], h};
                    if(res.isEmpty() || res.get(res.size() - 1)[1] != pos[1]) {// skip same level points
                        res.add(pos);
                    }
                    s ++;
                    t ++;
                    l += 2;
                }
                else {
                    h2 = right.get(t)[1];
                    h = Math.max(h1, h2);
                    int[] pos = {right.get(t)[0], h};
                    if(res.isEmpty() || res.get(res.size() - 1)[1] != pos[1]) {// skip same level points
                        res.add(pos);
                    }
                    t ++;
                    l ++;
                }
            }
            return res;
        }
    }
}
