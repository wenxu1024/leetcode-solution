#! /usr/bin/python

class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.l = []
        self.lmin = []
        
    def push(self, x):
        if len(self.l) == 0:
            self.l.append(x)
            self.lmin.append(x)
        else:
            if x <= self.lmin[-1]:
                self.lmin.append(x)
            self.l.append(x)
        
        

    # @return nothing
    def pop(self):
        if self.l[-1] == self.lmin[-1]:
            self.l.pop()
            self.lmin.pop()
        else:
            self.l.pop()
        

    # @return an integer
    def top(self):
        return self.l[-1]

    # @return an integer
    def getMin(self):
        return self.lmin[-1]


if __name__ == "__main__":
    mS = MinStack()
    mS.push(1)
    mS.push(2)
    mS.push(-1)
    print mS.getMin()
    mS.pop()
    print mS.getMin()
    mS.pop()
    print mS.getMin()
   
