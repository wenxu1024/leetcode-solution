import java.util.*;

public class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        int i, j, m, n;
        Trie t = new Trie();
        for (i = 0; i < words.length; i ++) {
            t.add(words[i]);
        }

	for (i = 0; i < words.length; i ++) System.out.println(t.search(words[i]));
        m = board.length; n = board[0].length;
        boolean[][] visited = new boolean[m][n];
        for(i = 0; i < m; i ++) {
            for(j = 0; j < n; j ++) {
                visited[i][j] = false;
            }
        }
        String s;
        List<String> res = new ArrayList<String> ();
        HashSet<String> hs = new HashSet<String> ();
        for(i = 0; i < m; i ++) {
            for(j = 0; j < n; j ++) {
                s = "";
                dfs_visit(board, t.root, i, j, hs, s, visited);
		for(int k = 0; k < m; k ++) System.out.println(Arrays.toString(visited[k]));
            }
        }
//	dfs_visit(board,t.root,0,0,hs,s,visited);
//	for(int k = 0; k < m; k ++) System.out.println(Arrays.toString(visited[k]));
        for(String si : hs) {
            res.add(si);
        }
        return res;
    }
    
    public void dfs_visit(char[][]board, TrieNode current, int i, int j, HashSet<String> hs, String s, boolean[][] visited) {
	if (visited[i][j] == true) {visited[i][j] = false; return;}
	visited[i][j] = true;
        int m, n;
        m = board.length;
        n = board[0].length;
        
        int k, p, l = current.child.size();
        
        for(k = 0; k < l; k ++) {
            if(current.child.get(k).c == board[i][j]) {
                s += board[i][j];
                current = current.child.get(k);
		for(p = 0; p < current.child.size(); p ++) {
			if(current.child.get(p).c == '$') {
				if(!hs.contains(s)) hs.add(s);
				break;
			}
		}
                if (i + 1 < m && !visited[i + 1][j]) dfs_visit(board, current, i + 1, j, hs, s, visited);
                if (i - 1 >= 0 && !visited[i - 1][j]) dfs_visit(board, current, i - 1, j, hs, s, visited);
                if (j + 1 < n && !visited[i][j + 1]) dfs_visit(board, current, i, j + 1, hs, s, visited);
                if (j - 1 >= 0 && !visited[i][j - 1]) dfs_visit(board, current, i, j - 1, hs, s, visited);
                break;
            }
        }
	visited[i][j] = false;//backtracking
        return;
    }


    public static void main(String[] args) {
        //char[][] board = {{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}};
        //String[] words = {"oath","pea","eat","rain"};
	//char[][] board = {{'a','a','a','a'}, {'a','a','a','a'},{'a','a','a','a'}};
	//String[] words = {"aaaaaaaaaaaa","aaaaaaaaaaaaa","aaaaaaaaaaab"};
	char[][] board = {{'a','b'},{'c','d'}};
	String[] words = {"ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"};
        System.out.println(Arrays.toString(words));
        for(int i = 0; i < board.length; i ++) System.out.println(Arrays.toString(board[i]));
        Solution sol = new Solution();
        System.out.println(sol.findWords(board, words));
    }   


}






class Trie {
    TrieNode root;
    
    public Trie() {
        root = new TrieNode(' ');
    }
    
    public void add(String s) {
        TrieNode current = root;
        int i, j, l;
        for(i = 0; i < s.length(); i ++) {
	    l = current.child.size();
            for(j = 0; j < l; j ++) {
                if (current.child.get(j).c == s.charAt(i)) {
                    current = current.child.get(j);
                    break;
                }
            }
            if (j == l) {
                TrieNode children = new TrieNode(s.charAt(i));
                current.child.add(children);
                current = children;
            }
        }
        if(i == s.length()) {
            for(j = 0; j <current.child.size(); j ++) {
                if(current.child.get(j).c == '$') {
                    break;
                }
            }
            if (j == current.child.size()) {
                TrieNode children = new TrieNode('$');
                current.child.add(children);
                current = children;
            }
        }
    }
    
    public boolean search(String s) {
        TrieNode current = root;
        int i, j, l;
        for(i = 0; i < s.length(); i ++) {
	    l = current.child.size();
            for(j = 0; j < l; j ++) {
                if (current.child.get(j).c == s.charAt(i)) {
                    current = current.child.get(j);
                    break;
                }
            }
            if (j == l) {
                return false;
            }
        }
        if (i == s.length()) {
            for(j = 0; j < current.child.size(); j ++) {
                if(current.child.get(j).c == '$') {
                    return true;
                }
            }
        }
        return false;
    }
}


class TrieNode {
    char c;
    List<TrieNode> child;
    
    public TrieNode(char c) {
        this.c = c;
        this.child = new ArrayList<TrieNode> ();
    }
}
