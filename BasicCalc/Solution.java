public class Solution {
    public int calculate(String s) {
        ArrayList<String> parsed = parse(s);
        ArrayList<String> rpn = toRPN(parsed);
        Stack<Integer> st = new Stack<Integer> ();
        int l = rpn.size();
        for(int i = 0; i < l; i ++) {
            String si = rpn.get(i);
            if (si.equals("+") || si.equals("-")) {
                if(si.equals("+")) {
                    int num2 = st.pop();
                    int num1 = st.pop();
                    int num = num1 + num2;
                    st.push(num);
                }
                else {
                    int num2 = st.pop();
                    int num1 = st.pop();
                    int num = num1 - num2;
                    st.push(num);
                }
            }
            else {
                int num = Integer.parseInt(si);
                st.push(num);
            }
        }
        int ans = st.pop();
        return ans;
    }
    
    public ArrayList<String> parse(String s) {
        ArrayList<String> res = new ArrayList<String> ();
        int l = s.length();
        String temp = "";
        for(int i = 0; i < l ; i ++) {
            if (s.charAt(i) == '(' || s.charAt(i) == ')' || s.charAt(i) == '+' || s.charAt(i) == '-') {
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
            if(si.equals("(") || si.equals("+") || si.equals("-")) {
                op.push(parsed.get(i));
            }
            else if (si.equals(")")) {
                while(!op.peek().equals("(")) {
                    res.add(op.pop());
                }
                op.pop();
                while(!op.isEmpty() && !op.peek().equals("(")) {
                    res.add(op.pop());
                }
            }
            else {
                res.add(si);
                while(!op.isEmpty() && !op.peek().equals("(")) {
                    res.add(op.pop());
                }
            }
        }
        while(!op.isEmpty()) {
            res.add(op.pop());
        }
        return res;
    }
}
