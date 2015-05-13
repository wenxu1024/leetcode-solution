public class Solution {
    
    private int f; // finishing time
    
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        this.f = 0;
        int[] ftime = new int[numCourses];
        Integer[] course = new Integer[numCourses];
        HashMap<Integer, Character> m = new HashMap<Integer, Character> ();
        int i;
        for(i = 0; i < numCourses; i ++) {
            m.put(i, 'w');
            course[i] = i;
        }
        for(i = 0; i < numCourses; i ++) {
            if (m.get(i) == 'w') {
                dfs_visit(i, prerequisites, m, ftime);
            }
        }
        Arrays.sort(course, new Comparator<Integer> () {
            @Override
            public int compare(Integer i1, Integer i2) {
                if (ftime[i1] == ftime[i2]) return 0;
                else if(ftime[i1] < ftime[i2]) return -1;
                else return 1;
            }
        });
        
        this.f = 0;
        int prev;
        for(i = 0; i < numCourses; i ++) {
            m.put(i, 'w');
        }
        for(i = 0; i < numCourses; i ++) {
            prev = this.f;
            dfs_visit(course[i], prerequisites, m, ftime);
            if (this.f - prev > 1) return (new int[0]);
            else prev = this.f;
        }
        
        int[] res = new int[numCourses];
        for(i = 0; i < numCourses; i ++) {
            res[i] = course[i];
        }
        return res;
    }
    
    public void dfs_visit(int currCourse, int[][] prerequisites, HashMap<Integer, Character> m, int[] ftime) {
        if (m.get(currCourse) == 'w') {
            m.put(currCourse, 'g');
            int l = prerequisites.length;
            for(int i = 0; i < l; i ++) {
                if(prerequisites[i][0] == currCourse && m.get(prerequisites[i][1]) == 'w') {
                    dfs_visit(prerequisites[i][1], prerequisites, m, ftime);
                }
            }
        }
        m.put(currCourse, 'b');
        ftime[currCourse] = this.f;
        this.f ++;
        return;
    }
}
