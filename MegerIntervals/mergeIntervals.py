#! /usr/bin/python
# Definition for an interval.
class Interval:
    def __init__(self,s=0,e=0):
        self.start=s
        self.end=e
    
    def __repr__(self):
        return '['+str(self.start)+','+str(self.end)+']'

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals=sorted(intervals,key=self.left)
        rinterval=[]
        if not intervals: 
            return intervals
        rinterval.append(intervals[0])
        for item in intervals:
            if item.start>rinterval[-1].end:
                rinterval.append(item)
            else:
                top=rinterval.pop()
                if item.end>top.end:
                    top.end=item.end
                    rinterval.append(top)
                else:
                    rinterval.append(top)
        return rinterval
            
        
                
        
    def left(self,item):
        return item.start

if __name__=='__main__':
    i1=Interval(1,3)
    i2=Interval(2,6)
    i3=Interval(8,10)
    i4=Interval(15,18)
    intervals=[i1,i2,i3,i4]
    s=Solution()
    print s.merge(intervals)

