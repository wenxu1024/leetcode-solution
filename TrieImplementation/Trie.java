class TrieNode {
    // Initialize your data structure here.
    public char key;
    public ArrayList<TrieNode> child;
    public TrieNode(char key) {
        this.key = key;
        this.child = null;
    }
}

public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode(' ');
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        int l = word.length();
        int i, m, j, k;
        TrieNode current;
        current = this.root;
        for (i = 0; i < l; i ++) {
            if (current.child == null) break;
            else {
                m = current.child.size();
                for (j = 0; j < m; j ++) {
                    if (word.charAt(i) == current.child.get(j).key) {
                        current = current.child.get(j);
                        break;
                    }
                }
                if (j == m) break;
            }
        }
        for (k = i; k < l; k ++) {
            if (current.child == null) current.child = new ArrayList<TrieNode> ();
            TrieNode t = new TrieNode(word.charAt(k));
            current.child.add(t);
            current = t;
        }
        TrieNode leaf = new TrieNode('$');
        if(current.child == null) current.child = new ArrayList<TrieNode> ();
        current.child.add(leaf);
        return;
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        TrieNode current = this.root;
        int l = word.length();
        int i, j, k, m;
        for (i = 0; i < l; i ++) {
            if (current.child == null) return false;
            else {
                m = current.child.size();
                for(j = 0; j < m; j ++) {
                    if (word.charAt(i) == current.child.get(j).key) {
                        current = current.child.get(j);
                        break;
                    }
                }
                if (j == m) return false;
            }
        }
        m = current.child.size();
        for (i = 0; i < m; i ++) {
            if (current.child.get(i).key == '$') return true;
        }
        return false;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
        TrieNode current = this.root;
        int l = prefix.length();
        int i, j, k, m;
        for (i = 0; i < l; i ++) {
            if (current.child == null) return false;
            else {
                m = current.child.size();
                for(j = 0; j < m; j ++) {
                    if (prefix.charAt(i) == current.child.get(j).key) {
                        current = current.child.get(j);
                        break;
                    }
                }
                if (j == m) return false;
            }
        }
        return true;
    }
}

// Your Trie object will be instantiated and called as such:
// Trie trie = new Trie();
// trie.insert("somestring");
// trie.search("key");
