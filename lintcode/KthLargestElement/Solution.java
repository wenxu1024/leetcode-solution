import java.util.*;

//Kth larest element

class Solution {
    //param k : description of k
    //param numbers : array of numbers
    //return: description of return
    public int kthLargestElement(int k, ArrayList<Integer> numbers) {
        // write your code here
        int n = numbers.size();
        return kthLargestElementHelper(numbers, n - k + 1, 0, n - 1);
    }
    
    public int kthLargestElementHelper(ArrayList<Integer> numbers, int rank, int i, int j) {
        int r = QSelect(numbers, i, j);
	System.out.println("r" + r);
        if (r == rank) return numbers.get(i + r - 1).intValue(); //if current element is the desired rank, output
        else if (r < rank) {
            return kthLargestElementHelper(numbers, rank - r, i + r, j); //current rank smaller
        }
        else {
            return kthLargestElementHelper(numbers, rank, i, i + r - 2); //current rank larger
        }
    }
    
    public static void swap(ArrayList<Integer> numbers, int i, int j) {
        Integer temp;
        temp = numbers.get(i);
        numbers.set(i, numbers.get(j));
        numbers.set(j, temp);
    }
    
    public int QSelect(ArrayList<Integer> numbers, int i, int j) { //Randomized Quick Select
        Random r = new Random();
//	r.setSeed(20);
        int l = (j - i + 1);
        int s;
        s = i + Math.abs(r.nextInt()) % l;
	System.out.println("s" + s);
        swap(numbers, i, s);
        s = i + 1;
	int t = s;
	while (t < j + 1) {
	    if (numbers.get(t).intValue() < numbers.get(i).intValue()) {
		swap(numbers, s, t);
		s ++;
		t ++;
	    }
	    else {
		t ++;
	    }
        }
        swap(numbers, i, s - 1);
        return s - i;
    }


    public static void main(String[] args) {
	ArrayList<Integer> l = new ArrayList<Integer> ();
        l.add(new Integer(9));
	l.add(new Integer(3));
	l.add(new Integer(2));
	l.add(new Integer(4));
	l.add(new Integer(8));
	int k = 3;
	Solution sol = new Solution();
	System.out.println(sol.kthLargestElement(k, l));
    }
};



