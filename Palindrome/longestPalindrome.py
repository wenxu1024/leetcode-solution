#! /usr/bin/python

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        l = len(s)
        start = 0
        longestlength = 0
        p =[[False for j in range(l)] for i in range(l)]
        for i in range(l):
            p[i][i] = True
        for i in range(l - 1):
            p[i][i + 1] = (s[i] == s[j])
        for length in range(3, l + 1):
            for i in range(l - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    p[i][j] = (p[i + 1][j - 1])
                else:
                    p[i][j] = False
                if p[i][j] == True:
                    start = i
                    longestlength = length
        return s[start : longestlength + start]
        
        
                    
            
if __name__ == "__main__":
     s = "jhgtrclvzumufurdemsogfkpzcwgyepdwucnxrsubrxadnenhvjyglxnhowncsubvdtftccomjufwhjupcuuvelblcdnuchuppqpcujernplvmombpdttfjowcujvxknzbwmdedjydxvwykbbamfnsyzcozlixdgoliddoejurusnrcdbqkfdxsoxxzlhgyiprujvvwgqlzredkwahexewlnvqcwfyahjpeiucnhsdhnxtgizgpqphunlgikogmsffexaeftzhblpdxrxgsmeascmqngmwbotycbjmwrngemxpfakrwcdndanouyhnnrygvntrhcuxgvpgjafijlrewfhqrguwhdepwlxvrakyqgstoyruyzohlvvdhvqmzdsnbtlwctetwyrhhktkhhobsojiyuydknvtxmjewvssegrtmshxuvzcbrabntjqulxkjazrsgbpqnrsxqflvbvzywzetrmoydodrrhnhdzlajzvnkrcylkfmsdode"
     sol = Solution()
     print sol.longestPalindrome(s)
