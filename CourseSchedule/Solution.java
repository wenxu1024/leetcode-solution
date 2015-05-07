import java.util.*;

public class Solution {
    private int f; // finishing time
    private int count; // size of strongly connected components
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        //find the strongly connected components
        //if there exists one SCC whose size > 1, then return false, otherwise return true
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
	    if(m.get(i) == 'w') {
                dfs_visit(i, prerequisites, m, ftime);
	    }
        }
//	System.out.println(Arrays.toString(ftime));
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
            if (this.f - prev > 1) return false;
            else prev = this.f;
        }
        return true;
    }
    
    public void dfs_visit(int currCourse, int[][] prerequisites, HashMap<Integer, Character> m, int[] ftime) {
        if (m.get(currCourse) == 'w') {
            m.put(currCourse, 'g');
            int l = prerequisites.length;
            for(int i = 0; i < l; i ++) {
	//	System.out.println(i + "   " + l + Arrays.toString(prerequisites[i]) + m);
                if(prerequisites[i][0] == currCourse && m.get(prerequisites[i][1]) == 'w') {
                    dfs_visit(prerequisites[i][1], prerequisites, m, ftime);
                }
            }
        }
	m.put(currCourse, 'b');
	ftime[currCourse] = this.f;
//	System.out.println(currCourse + ","+this.f);
	this.f ++;
        return;
    }

    public static void main(String[] args) {
	int numCourses = 8;
	int [][] prerequisites = {{1, 0}, {2, 6}, {1, 7}, {6, 4}, {7, 0}, {0, 5}};
//	int[][] prerequisites = {{0, 1}};
	Solution s = new Solution();
//	System.out.println(numCourses);
	//System.out.println(Arrays.toString(prerequisites[1]));
	System.out.println(s.canFinish(numCourses, prerequisites));
    }
}
