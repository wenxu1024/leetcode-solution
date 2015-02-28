import java.util.*;
// binary representation

public class Solution {
        public String binaryRepresentation(String n) {
                //remove trailing zeroes
                int i, l, k = 0;
                l = n.length();
                String temp = "";
                for (i = l - 1; i > -1; i --) {
                    if (n.charAt(i) != '0') {k = i; break;}
                }
                for (i = 0; i < k + 1; i ++) {
                    temp += n.charAt(i);
                }
                n = temp;
                String decimal = getDecimal(n);
                String integer = getInteger(n);
                String res;
                res = "";
                res += integer;
                if (decimal != "") res += '.';
                int count = 0;
                while(decimal != "") {
                        if (count > 128) return "ERROR";
                        n = multi2(decimal);
			System.out.println(n +"->"+ res);
                        integer = getInteger(n);
                        decimal = getDecimal(n);
                        res += integer;
                        count ++;
                }
                return res;
        }

        public String getDecimal(String n) {
                String res;
                res = "";
                int l = n.length();
                int i;
                boolean state = false;
                for(i = 0; i < l; i++) {
                        if (n.charAt(i) == '.') {state = true; continue;}
                        if (state == true) res += n.charAt(i);
                }
                return res;
        }
        
        
        public String getInteger(String n) {
                String res;
                res = "";
                int l = n.length();
                int i;
                for (i = 0; i < l; i ++) {
                        if (n.charAt(i) != '.') res += n.charAt(i);
                        else break;
                }
                int dec = Integer.parseInt(res);
                return Integer.toString(dec, 2);
        }

        public String multi2(String n) {
        int l = n.length();
        String res, temp; // multiply 2 then remove trailing zeros.
        int i, d, carry = 0;
        char c;
        res = "";
        temp = "";
        for (i = l - 1; i > -1; i--) {
            d = n.charAt(i) - '0';
            if (d * 2 + carry < 10) {
                d = (d * 2 + carry) + '0';
                c = (char) d;
                res += c;
                carry = 0;
            }
            else {
                d = (d * 2 + carry - 10) + '0';
                c = (char) d;
                res += c;
                carry = 1;
            }
        }
        res += '.';
        res += (char) (carry + '0');
        l = res.length();
        int k = 0;
        for (i = 0; i < l; i ++) {
            if (res.charAt(i) != '0') {
                k = i;
                break;
            }
        }
        //reverse and drop trailing zeroes.
        for (i = l - 1; i > k - 1; i --) {
            temp += res.charAt(i);
        }
        return temp;
    }

	public static void main(String[] args) {
		String n = "0.125";
		Solution sol = new Solution();
//	        String decimal = sol.getDecimal(n);
//		String integer = sol.getInteger(n);
//		System.out.println(integer);
//		System.out.println(decimal);
//		System.out.println(sol.multi2(decimal));
		System.out.println(sol.binaryRepresentation(n));
	}
};
