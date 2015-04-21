public class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        if (m == 0) return 0;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        int i,j;
        for(i = 0; i < m; i++) {
            for(j = 0; j < n; j++) {
                visited[i][j] = false;
            }
        }
        int count = 0;
        for(i = 0; i < m; i ++) {
            for(j = 0; j < n; j ++) {
                if (grid[i][j] == '1' && visited[i][j] == false) {
                    count ++;
                    dfs_visit(grid,i,j,visited, m, n);
                }
            }
        }
        return count;
    }
    
    
    private void dfs_visit(char[][] grid, int i, int j, boolean[][] visited, int m, int n) {
        if (visited[i][j] == true) return;
        visited[i][j] = true;
        if (i + 1 < m && grid[i + 1][j] == '1') dfs_visit(grid, i + 1, j, visited, m, n);
        if (i - 1 >= 0 && grid[i - 1][j] == '1') dfs_visit(grid, i - 1, j, visited, m, n);
        if (j + 1 < n && grid[i][j + 1] == '1') dfs_visit(grid, i, j + 1, visited, m, n);
        if (j - 1 >= 0 && grid[i][j - 1] == '1') dfs_visit(grid, i, j - 1, visited, m, n);
        return;
    }
}
