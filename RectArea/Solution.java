public class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int rec1 = (C - A) * (D - B);
        int rec2 = (G - E) * (H - F);
        int res;
        res = rec1 + rec2 - intersection(A, B, C, D, E, F, G, H);
        return res;
    }
    
    public int intersection(int A, int B, int C, int D, int E, int F, int G, int H) {
        if (H <= B) return 0;
        else {
            if (F >= D) return 0;
            else {
                int height = Math.min(D, H) - Math.max(B, F);
                if (G <= A) return 0;
                else {
                    if (E >= C) return 0;
                    else {
                        int width = Math.min(C, G) - Math.max(E, A);
                        return height * width;
                    }
                }
            }
        }
    }
}
