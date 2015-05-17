import java.util.*;

public class Solution {
    /**
     * @param expression: A string array
     * @return: The Reverse Polish notation of this expression
     */
    public ArrayList<String> convertToRPN(String[] expression) {
        // write your code here
        // Shunting yard algorithm
        Stack<String> s = new Stack<String> ();
        ArrayList<String> output = new ArrayList<String> ();
        HashMap<String,Integer> precedence = new HashMap<String,Integer> ();
        precedence.put("+", 1); precedence.put("-", 1);
        precedence.put("*", 2); precedence.put("/", 2);
        int l = expression.length;
        int i;
        for(i = 0; i < l; i ++) {
	    System.out.println(s);
	    System.out.println(output);
            if(isOperand(expression[i])) {
                output.add(expression[i]);
            }
            else {
                if (expression[i].equals("(")) s.push(expression[i]);
                else if (expression[i].equals(")")) {
                    while(!s.peek().equals("(")) {
                        output.add(s.pop());
                    }
                    s.pop();
                }
                else {
                    while(!s.empty()) {
                        if(precedence.containsKey(s.peek()) && precedence.get(expression[i]) <= precedence.get(s.peek())) output.add(s.pop());
                        else break;
                    }
                    s.push(expression[i]);
                }
            }
        }
        while(!s.empty()) {
            output.add(s.pop());
        }
        return output;
    }
    
    private boolean isOperand(String s) {
        if (s.equals("(")) return false;
        if (s.equals(")")) return false;
        if (s.equals("+")) return false;
        if (s.equals("-")) return false;
        if (s.equals("*")) return false;
        if (s.equals("/")) return false;
        return true;
    }

    public static void main(String[] args) {
	String[] expression = {"2","*","6","-","(","23","+","7",")","/","(","1","+","2",")"};
	Solution sol = new Solution();
	System.out.println(sol.convertToRPN(expression));
    }
}


