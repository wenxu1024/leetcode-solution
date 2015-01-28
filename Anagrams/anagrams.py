#! /usr/bin/python

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        l = len(strs)
        if l < 2:
            return []
        strs = sorted(strs, key = self.sort)   # sort the string alphabetically, then sort the list alphabetically
        i = 0
        res = []
        c = 1  # record the anagrams group size
        for j in range(1, l): # scan the list
            s1 = strs[i]
            s2 = strs[j]
            if ''.join(sorted(s1)) == ''.join(sorted(s2)):
                res.append(s2)
                c += 1  #if is anagrams, increase the count
            else:
                if c > 1:  # if the anagrams group count larger than 1, add the root anagram
                    res.append(strs[i])
                i = j # else skip , update the root anagram
                c = 1 # update the count
        if c > 1: # if the count is greater than 1 after the scan terminates, add the root anagram
            res.append(strs[i])
        return res

    def isAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        l = len(s1)
        for i in range(l):
            if s1[i] != s2[i]:
                return False
        return True
        
        
    def sort(self, s):  # sort each string alphabetically
        return ''.join(sorted(s))


if __name__ == "__main__":
    strs = ['tea', 'ate', 'it', 'ti', 'able', 'elba']
    sol = Solution()
    print sol.anagrams(strs)
