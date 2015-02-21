import java.util.*;

// Soluiton to word search II using trie and dfs.

public class Solution {
    /**
     * @param board: A list of lists of character
     * @param words: A list of string
     * @return: A list of string
     */
    public ArrayList<String> wordSearchII(char[][] board, ArrayList<String> words) {
        // write your code here
        Trie t = new Trie();
        int i, j, m, n, l;
        l = words.size();
        m = board.length;
        n = board[0].length;
        String s = "";
        boolean[][] visited = new boolean[m][n];
        for (i = 0; i < m; i ++) {
            for(j = 0; j < n; j ++) {
                visited[i][j] = false;
            }
        }
        for (i = 0; i < l; i ++) t.insert(words.get(i));
        TrieNode root = t.root;
        HashSet<String> res = new HashSet<String> ();
        for (i = 0; i < m; i ++) {
            for(j = 0; j < n; j ++) {
                s = "";
                wordSearchII_dfs(board, root, res, i, j, s, visited);
            }
        }
        //convert hashset to arraylist;
        ArrayList<String> arrayres = new ArrayList<String> ();
        Iterator<String> iterator = res.iterator();
        while (iterator.hasNext()) arrayres.add(iterator.next());
        return arrayres;
    }
    
    public void wordSearchII_dfs(char[][] board, TrieNode root, HashSet<String> res, int i, int j, String s, boolean[][] visited) {
        if (visited[i][j] == true) {visited[i][j] = false; return;}
        visited[i][j] = true;
        char c = board[i][j];
        s += c;
        int m = board.length;
        int n = board[0].length;
        if (root.subNode(c) == null) {visited[i][j] = false; return;}
        else {
            TrieNode child = root.subNode(c);
            if (child.isEnd == true) {
                res.add(s);
            }
            if (i + 1 < m && visited[i + 1][j] == false && child.subNode(board[i + 1][j]) != null) wordSearchII_dfs(board, child, res, i + 1, j, s, visited);
            if (i - 1 >= 0 && visited[i - 1][j] == false && child.subNode(board[i - 1][j]) != null) wordSearchII_dfs(board, child, res, i - 1, j, s, visited);
            if (j + 1 < n && visited[i][j + 1] == false && child.subNode(board[i][j + 1]) != null) wordSearchII_dfs(board, child, res, i, j + 1, s, visited);
            if (j - 1 >= 0 && visited[i][j - 1] == false && child.subNode(board[i][j - 1]) != null) wordSearchII_dfs(board, child, res, i, j - 1, s, visited);
        }
        visited[i][j] = false; //backtrack
        return;
    }
}



class TrieNode 
{
    char content; 
    boolean isEnd; 
    int count;  
    LinkedList<TrieNode> childList; 
 
    /* Constructor */
    public TrieNode(char c)
    {
        childList = new LinkedList<TrieNode>();
        isEnd = false;
        content = c;
        count = 0;
    }  
    public TrieNode subNode(char c)
    {
        if (childList != null)
            for (TrieNode eachChild : childList)
                if (eachChild.content == c)
                    return eachChild;
        return null;
    }
}
 
class Trie
{
    public TrieNode root;
 
     /* Constructor */
    public Trie()
    {
        root = new TrieNode(' '); 
    }
     /* Function to insert word */
    public void insert(String word)
    {
        if (search(word) == true) 
            return;        
        TrieNode current = root; 
        for (char ch : word.toCharArray() )
        {
            TrieNode child = current.subNode(ch);
            if (child != null)
                current = child;
            else 
            {
                 current.childList.add(new TrieNode(ch));
                 current = current.subNode(ch);
            }
            current.count++;
        }
        current.isEnd = true;
    }
    /* Function to search for word */
    public boolean search(String word)
    {
        TrieNode current = root;  
        for (char ch : word.toCharArray() )
        {
            if (current.subNode(ch) == null)
                return false;
            else
                current = current.subNode(ch);
        }      
        if (current.isEnd == true) 
            return true;
        return false;
    }
    /* Function to remove a word */
    public void remove(String word)
    {
        if (search(word) == false)
        {
            System.out.println(word +" does not exist in trie\n");
            return;
        }             
        TrieNode current = root;
        for (char ch : word.toCharArray()) 
        { 
            TrieNode child = current.subNode(ch);
            if (child.count == 1) 
            {
                current.childList.remove(child);
                return;
            } 
            else 
            {
                child.count--;
                current = child;
            }
        }
        current.isEnd = false;
    }
}    
