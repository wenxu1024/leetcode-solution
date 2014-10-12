#! /usr/bin/python
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        wordlist = []
        word = ''
        l = len(s)
        for i in range(l):
            if s[i] == ' ':
                if word != '':
                     wordlist += [word]
                word = ''
            else:
                word += s[i]
        if word != '':
            wordlist += [word]
        
        res = ''
        l = len(wordlist)
        wordlist.reverse()
        for i in range(l):
            res += (wordlist[i] + ' ')
	res = res[: -1]
        return res
        

if __name__ == '__main__':
    sol = Solution()
    s = "the sky is blue"
    print sol.reverseWords(s)
