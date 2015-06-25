#! /usr/bin/python 

class Solution:
    # amazon phone interview
    def repeat(self, str):
        l = len(str)
        if l < 4:
           return False
        for i in range(2,l):
           if str[i] != str[0]:
               break
        else:
           return False
           
        for i in range(2,l):
           if str[i] == str[0]:
               if l % i == 0:
                  for j in range(i,l):
                     d = j % i
                     if str[j] != str[d]:
                         break   
                  else:
                     return True     
        return False
 


if __name__ == "__main__":
    l = ["aaabaaaaba","abcabcabc", "bcdbcdbcde", "abcdabcd", "xyz", "aaaaaaaaa"]
    sol = Solution()
    for item in l:
       print l, sol.repeat(item)
