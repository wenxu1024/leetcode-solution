import java.util.*;

public class Solution {
    public int calculate(String s) {
        ArrayList<String> parsed = parse(s);
        ArrayList<String> rpn = toRPN(parsed);
        Stack<Long> st = new Stack<Long> ();
        int l = rpn.size();
        for(int i = 0; i < l; i ++) {
            String si = rpn.get(i);
            if (si.equals("+") || si.equals("-") || si.equals("*") || si.equals("/")) {
                if(si.equals("+")) {
                    long num2 = st.pop();
                    long num1 = st.pop();
                    long num = num1 + num2;
                    st.push(num);
                }
                else if(si.equals("-")) {
                    long num2 = st.pop();
                    long num1 = st.pop();
                    long num = num1 - num2;
                    st.push(num);
                }
                else if(si.equals("*")) {
                    long num2 = st.pop();
                    long num1 = st.pop();
                    long num = num1 * num2;
                    st.push(num);
                }
                else {
                    long num2 = st.pop();
                    long num1 = st.pop();
                    long num = num1 / num2;
                    st.push(num);
                }
            }
            else {
                long num = Long.parseLong(si);
                st.push(num);
            }
        }
        int ans = st.pop().intValue();
        return ans;
    }
    
    public ArrayList<String> parse(String s) {
        ArrayList<String> res = new ArrayList<String> ();
        int l = s.length();
        String temp = "";
        for(int i = 0; i < l ; i ++) {
            if (s.charAt(i) == '(' || s.charAt(i) == ')' || 
                s.charAt(i) == '+' || s.charAt(i) == '-' ||
                s.charAt(i) == '*' || s.charAt(i) == '/') {
                 if (!temp.equals("")) res.add(temp);
                 String op = "";
                 op += s.charAt(i);
                 res.add(op);
                 temp = "";
            }
            else {
                if(s.charAt(i) != ' ') temp += s.charAt(i);
            }
        }
        if (!temp.equals("")) res.add(temp);
        return res;
    }
    
    public ArrayList<String> toRPN(ArrayList<String> parsed) {
        //shunting yard algorithm
        Stack<String> op = new Stack<String> ();
        ArrayList<String> res = new ArrayList<String> ();
        int l = parsed.size();
        for(int i = 0; i < l; i ++) {
            String si = parsed.get(i);
            if(si.equals("(")) {
                op.push(parsed.get(i));
            }
            else if (si.equals("*") || si.equals("/")) {
                while(!op.isEmpty() && !op.peek().equals("(") && !op.peek().equals("+") && !op.peek().equals("-")) {
                    res.add(op.pop());
                }
                op.push(parsed.get(i));
            }
            else if (si.equals("+") || si.equals("-")) {
                while(!op.isEmpty() && !op.peek().equals("(")) {
                    res.add(op.pop());
                }
                op.push(parsed.get(i));
            }
            else if (si.equals(")")) {
                while(!op.peek().equals("(")) {
                    res.add(op.pop());
                }
                op.pop();
            }
            else {
                res.add(parsed.get(i));
            }
        }
        while(!op.isEmpty()) {
            res.add(op.pop());
        }
        return res;
    }    

    public static void main(String[] args) {
//	String s = "(4 + 9)";
	String s = "0-2147483648";
	Solution sol = new Solution();
	System.out.println(sol.parse(s));
	System.out.println(sol.toRPN(sol.parse(s)));
	System.out.println(sol.calculate(s));
    }
}
