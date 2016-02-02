#! /usr/bin/python

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = self.parseStringToList(preorder)
        return self.isValidSerializationHelper(preorder)
        
#    def isValidSerializationHelper(self, preorder): Recursive Solution
#        l = len(preorder)
#        if l == 1:
#            return preorder[0] == "#"
#        else:
#            if preorder[0] > '9' or preorder[0] < '0':
#                return False
#            else:
#                if l < 3:
#                    return False
#                for i in range(2, l):
#                    preorder_left = preorder[1:i]
#                    preorder_right = preorder[i:]
#                    if self.isValidSerializationHelper(preorder_left) and self.isValidSerializationHelper(preorder_right):
#                        return True
#                return False
 
 
#    def isValidSerializationHelper(self, preorder):    # Dynamic programming solution           
#        l = len(preorder)
#        C = [[False for i in range(l)] for j in range(l)]
#        for i in xrange(l - 1, -1, -1):
#            for j in xrange(i + 1, l, 1):
#                if i == j:
#                    if preorder[i] == "#":
#                        C[i][j] = True
#                    else:
#                        C[i][j] = False
#                else:
#                    if preorder[i] > '9' or preorder[i] < '0':
#                        C[i][j] = False
#                    else:
#                        if (j - i + 1) < 3:
#                            C[i][j] = False
#                        else:
#                            for k in range(i + 2, j):
#                                if C[i + 1][k - 1] and C[k][j]:
#                                    C[i][j] = True
#                                    break
#                            else:
#                                C[i][j] = False
#        return C[0][l - 1]

    def isValidSerializationHelper(self, preorder):
        l = len(preorder)
        stack = []
        if l == 0:
            return False
        for i in range(l - 1, -1, -1):
            if preorder[i] == "#":
                stack.append(True)
            else:
                if len(stack) < 2:
                    return False
                else:
                    stack.pop()
                    stack.pop()
                    stack.append(True)
        if len(stack) == 1 and stack[0] == True:
            return True
        else:
            return False
                
    def parseStringToList(self, preorder):
        res = []
        s = ""
        l = len(preorder)
        for i in range(l):
            if preorder[i] == ",":
                res += [s]
                s = ""
            else:
                s += preorder[i]
        res += [s]
        return res

if __name__ == "__main__":
    preorder = "9,9,9,9,#,9,#,#,9,#,9,9,#,9,#,#,#,9,9,9,9,9,9,#,#,#,9,9,9,#,#,9,9,#,#,9,#,#,#,9,9,9,9,#,9,#,#,9,9,#,9,9,9,#,#,#,#,9,9,#,#,9,#,#,9,9,9,#,#,#,9,#,9,9,#,#,9,#,9,#,#,#,9,9,9,9,9,#,#,9,9,#,9,9,9,#,9,#,#,9,#,#,#,#,9,9,#,9,9,9,9,9,#,#,9,#,#,9,9,#,#,#,#,9,9,9,#,#,#,9,#,#,9,9,9,9,9,#,#,9,9,#,#,#,#,9,9,9,#,#,9,#,#,#,9,9,#,#,9,#,9,#,9,#,#,#,9,9,9,9,#,#,#,9,9,9,9,9,#,#,#,9,9,#,9,#,9,#,#,9,9,#,#,9,#,#,9,#,#,9,#,9,#,#,9,9,9,9,9,9,#,#,9,9,9,#,#,9,#,#,9,9,9,#,#,9,#,9,#,9,#,#,9,#,9,#,#,#,9,#,9,#,#,9,9,#,#,9,9,9,#,#,#,9,9,#,#,#,#,9,9,9,9,#,#,9,9,#,#,#,9,9,9,#,9,#,#,9,#,#,9,9,9,#,#,#,#,9,9,#,#,9,#,#,9,9,9,9,9,#,#,9,9,#,#,9,#,#,9,9,9,9,9,#,#,#,9,#,9,#,9,9,#,#,#,9,9,9,#,#,9,#,#,#,9,9,9,#,#,9,9,9,9,#,#,#,9,#,#,9,#,9,9,#,#,9,9,#,#,#,9,#,#,9,9,9,9,9,9,9,9,9,9,9,#,9,#,#,9,#,#,9,9,#,#,9,#,9,#,9,#,#,9,#,#,9,9,9,9,#,#,9,#,#,9,9,#,#,9,9,#,#,9,#,#,#,9,9,#,9,9,#,9,9,#,#,9,#,#,9,9,#,9,#,#,#,#,9,9,9,9,#,#,#,9,9,#,#,#,#,9,#,#,9,#,9,9,9,#,#,9,9,9,9,#,#,9,#,#,9,9,#,#,9,#,#,9,9,9,#,#,#,9,#,#,9,#,9,#,9,9,#,#,#,#,9,9,9,9,#,#,#,9,9,9,9,#,9,9,9,#,#,9,#,#,#,9,9,9,#,9,#,9,#,#,#,9,#,#,9,#,9,#,#,9,9,9,9,9,9,#,#,9,9,#,9,#,#,#,9,9,9,#,#,#,9,9,9,#,#,9,#,9,#,#,#,9,9,9,#,#,#,9,9,#,#,9,#,9,#,#,9,#,#,9,9,9,9,#,#,#,9,#,9,#,#,9,9,9,#,#,#,9,9,#,#,9,#,#,9,9,9,9,#,#,9,#,9,9,#,9,9,9,#,#,#,#,9,#,#,9,9,9,9,9,9,#,9,#,9,9,#,#,#,#,9,9,#,#,#,9,#,#,9,9,#,9,#,#,#,#,9,9,#,#,#,9,9,9,#,9,#,9,9,#,#,#,9,9,#,9,9,#,#,#,9,#,#,9,9,#,9,#,9,#,#,9,#,9,#,#" 
    #preorder = "9,#,#,1"
    #preorder = "1,#,#"
    sol = Solution()
    print sol.parseStringToList(preorder)
    print sol.isValidSerialization(preorder)

