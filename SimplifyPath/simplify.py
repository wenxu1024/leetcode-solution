#! /usr/bin/python

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        if path[0] != '/':
            path = '/' + path    # add prevailing '/' if missing
        else:
            if path[-1] != '/':  # add trailing '/' if missing
                path = path + '/'
            else:
                pass
        lc = []
        stack = []
        l = len(path)
        d = ''
        for i in range(1, l):
            if path[i] == '/':
                if d != '':
                    lc.append(d)   #store string segement separated by '/' if segment is not empty
                d = ''
            else:
                d = d + path[i]
        n = len(lc)
        for i in range(n):
            if lc[i] == '.':   # if segment is '.', skip that segment
                pass
            elif lc[i] == "..":
                if stack == []:  # if already the highest directory (stack empty), don't do anything
                    pass
                else:
                    stack.pop() # if not highest directory, move to parent directory, pop the lowest directory
            else:
                stack.append(lc[i])
        res = ''
        if stack == []:
            return '/'
        for item in stack:
            res = res + '/' + item
        return res 

if __name__ == "__main__":
     path1 = '/.../'
     path2 = '/home'
     path3 = '/abc/.../../'
     path4 = "../SimplifyPath/.././../../leetcode/leetcode-solution/SimplifyPath/../../"
     path = [path1, path2, path3, path4]
     sol = Solution()
     for item in path:
        print sol.simplifyPath(item)
