#! /usr/bin/python

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
     
    def __str__(self):
        string = ""
        string = "(" + str(self.start) + "," + str(self.end) + ")"
        return string

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        l = len(intervals)
        if l == 0:
            return [newInterval]
        startindex = self.binarysearch_start(intervals, newInterval.start, 0, l - 1)
        endindex = self.binarysearch_end(intervals, newInterval.end, 0, l - 1)
        if startindex == 0 and endindex == l:
            return [newInterval]
            
        elif startindex == 0 and endindex < l:
            if intervals[endindex].start <= newInterval.end:
                mergeInterval = Interval(newInterval.start, intervals[endindex].end)
                res = [mergeInterval]
                for i in range(endindex + 1, l):
                    res.append(intervals[i])
                return res
            else:
                mergeInterval = Interval(newInterval.start, newInterval.end)
                res = [mergeInterval]
                for i in range(endindex, l):
                    res.append(intervals[i])
                return res
                
        elif startindex > 0 and endindex == l:
            if intervals[startindex - 1].end >= newInterval.start:
                mergeInterval = Interval(intervals[startindex - 1].start, newInterval.end)
                res = []
                for i in range(startindex - 1):
                    res.append(intervals[i])
                res.append(mergeInterval)
                return res
            else:
                mergeInterval = Interval(newInterval.start, newInterval.end)
                res = []
                for i in range(startindex):
                    res.append(intervals[i])
                res.append(mergeInterval)
                return res
        else:
            if intervals[startindex - 1].end >= newInterval.start and intervals[endindex].start <= newInterval.end:
                mergeInterval = Interval(intervals[startindex - 1].start, intervals[endindex].end)
                res = []
                for i in range(startindex - 1):
                    res.append(intervals[i])
                res.append(mergeInterval)
                for i in range(endindex + 1, l):
                    res.append(intervals[i])
                return res
            elif intervals[startindex - 1].end < newInterval.start and intervals[endindex].start <= newInterval.end:
                mergeInterval = Interval(newInterval.start, intervals[endindex].end)
                res = []
                for i in range(startindex):
                    res.append(intervals[i])
                res.append(mergeInterval)
                for i in range(endindex + 1, l):
                    res.append(intervals[i])
                return res
            elif intervals[startindex - 1].end >= newInterval.start and intervals[endindex].start > newInterval.end:
                mergeInterval = Interval(intervals[startindex - 1].start, newInterval.end)
                res = []
                for i in range(startindex - 1):
                    res.append(intervals[i])
                res.append(mergeInterval)
                for i in range(endindex, l):
                    res.append(intervals[i])
                return res
            else:
                mergeInterval = Interval(newInterval.start, newInterval.end)
                res = []
                for i in range(startindex):
                    res.append(intervals[i])
                res.append(mergeInterval)
                for i in range(endindex, l):
                    res.append(intervals[i])
                return res
            
                    
            
            
            
                
                
                
        
    def binarysearch_start(self, intervals, val, i, j):
        if i == j + 1:
            return i
        else:
            k = (i + j) / 2
            if intervals[k].start == val:
                return k
            elif intervals[k].start < val:
                return self.binarysearch_start(intervals, val, k + 1, j)
            else:
                return self.binarysearch_start(intervals, val, i, k - 1)
                
    def binarysearch_end(self, intervals, val, i, j):
        if i == j + 1:
            return i
        else:
            k = (i + j) / 2
            if intervals[k].end == val:
                return k
            elif intervals[k].end < val:
                return self.binarysearch_end(intervals, val, k + 1, j)
            else:
                return self.binarysearch_end(intervals, val, i, k - 1)
        

if __name__ == "__main__":
    sol = Solution()
    i1 = Interval(1,2)
    i2 = Interval(3,5)
    i3 = Interval(6,7)
    i4 = Interval(8, 10)
    i5 = Interval(12,16)
    i6 = Interval(4, 9)
    l = [i1, i2, i3, i4, i5]
    s = "["
    for item in l:
       s = s + str(item) + "  "
    s = s + "]"
    print s
    l = sol.insert(l, i6)
    s = "["
    for item in l:
       s = s + str(item) + "  "
    s = s + "]"
    print s
