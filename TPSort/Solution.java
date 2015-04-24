import java.util.*;

public class Solution {
	private int f;
	public ArrayList<Character> sort(ArrayList<Pair<Character, Character> > list) {
		HashMap<Character, Integer> m = new HashMap<Character, Integer> ();
		HashMap<Character, Character> visited = new HashMap<Character, Character> ();
		int l = list.size();
		int i,f;
	        this.f = 0;
		for(i = 0; i < l; i ++) {
			char ca = list.get(i).A;
			char cb = list.get(i).B;
			m.put(ca, 0);
			m.put(cb, 0);
			visited.put(ca, 'w');
			visited.put(cb, 'w');
		}
		for (char A : m.keySet()) {
			if (visited.get(A) == 'w') {
				dfs_visit(A, list, visited, m);
			}
		}
		System.out.println(m);
		ArrayList<Character> res = new ArrayList(m.keySet());
		Collections.sort(res, new Comparator<Character> () {
			@Override
			public int compare(Character A, Character B) {
				return m.get(A).compareTo(m.get(B));
			}
		        });
		return res;	
	}
			
	public void dfs_visit(char A, ArrayList<Pair<Character, Character> > list, HashMap<Character, Character> visited, HashMap<Character, Integer> m) {
		if (visited.get(A) == 'w') {
			visited.put(A, 'g');
			for (Pair<Character, Character> p : list) {
				if(p.A == A && visited.get(p.B) == 'w') {
					dfs_visit(p.B, list, visited, m);	
				}
			}
		}
		visited.put(A, 'b');
		m.put(A, this.f);
		this.f ++;
		return;
	}


	public static void main(String[] args) {
		Pair<Character, Character> p1 = new Pair('A', 'B');
		Pair<Character, Character> p2 = new Pair('B', 'C');
		Pair<Character, Character> p3 = new Pair('E', 'A');
		Pair<Character, Character> p4 = new Pair('Q', 'B');
		Pair<Character, Character> p5 = new Pair('Q', 'C');
		ArrayList<Pair<Character, Character> > list = new ArrayList<Pair<Character, Character> > ();
		list.add(p1); list.add(p2); list.add(p3); list.add(p4); list.add(p5);
		Solution s = new Solution();
		System.out.println(s.sort(list));
	}	
}

class Pair<K, T> {
	public K A;
	public T B;
	
	public Pair(K A, T B) {
		this.A = A;
		this.B = B;
	}
}
