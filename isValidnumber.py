class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        # use finte state machine
        state=0
        transitTable=[[0,2,4,-1,1],
                      [-1,2,4,-1,-1],
                      [9,2,3,6,-1],
                      [9,3,-1,6,-1],
                      [-1,5,-1,-1,-1],
                      [9,5,-1,6,-1],
                      [-1,8,-1,-1,7],
                      [-1,8,-1,-1,-1],
                      [9,8,-1,-1,-1],
                      [9,-1,-1,-1,-1]]
        l=len(s)
        for i in range(l):
            nextTolken=self.getTolken(s[i])
            if nextTolken==-1:
                return False
            state=transitTable[state][nextTolken]
            if state==-1:
                return False
        return state==2 or state==3 or state==5 or state==8 or state==9
            
    def getTolken(self,c):
        if c==' ' or c=='\t':
            return 0
        elif c>='0' and c<='9':
            return 1
        elif c=='.':
            return 2
        elif c=='e' or c=='E':
            return 3
        elif c=='+' or c=='-':
            return 4
        else:
            return -1
