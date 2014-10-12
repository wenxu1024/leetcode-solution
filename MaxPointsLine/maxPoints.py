#! /usr/bin/python

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        l=len(points)
        maxtally=0
        if l<=2:
            return l
        for i in range(l):
            for j in range(i):
		tally=2
                for k in range(l):
                    if k!=i and k!=j:
                        if points[k]==points[i] or points[k]==points[j]:
                            tally+=1
                        elif points[k].x==points[i].x and points[k].x==points[j].x:
                            tally+=1
                        elif points[k].y==points[i].y and points[k].y==points[j].y:
                            tally+=1
                        elif (points[k].x-points[i].x)*(points[k].y-points[j].y)==(points[k].x-points[j].x)*(points[k].y-points[i].y):
                            tally+=1
			else:
			    continue
                if tally>maxtally:
                    maxtally=tally
	return maxtally
                    
        
if __name__=='__main__':
     point1=Point(1,1)
     point2=Point(2,2)
     point3=Point(3,3)
     point4=Point(4,4)
     points=[point1,point2,point3,point4]
     sol=Solution()
     print sol.maxPoints(points)
