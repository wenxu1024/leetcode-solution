#! /usr/bin/python

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        l1 = []
        l2 = []
        res = ''
        for c in version1:
            if c != '.':
                res += c
            else:
                l1.append(int(res))
                res = ''
        l1.append(int(res))
        res = ''
        for c in version2:
            if c != '.':
                res += c
            else:
                l2.append(int(res))
                res = ''
        l2.append(int(res))
        n = min(len(l1), len(l2))
        for i in range(n):
            if l1[i] > l2[i]:
                return 1
            elif l1[i] < l2[i]:
                return -1
        if len(l1) == len(l2):
            return 0
        elif len(l1) > len(l2):
            for i in range(len(l2),len(l1)):
                if l1[i] != 0:
                    return 1
            return 0
        else:
            for i in range(len(l1),len(l2)):
                if l2[i] != 0:
                    return -1
            return 0
        
        
if __name__ == "__main__":
    version1 = "1.11.1.2"
    version2 = "1.02.3.4"
    sol = Solution()
    print sol.compareVersion(version1, version2)
  
