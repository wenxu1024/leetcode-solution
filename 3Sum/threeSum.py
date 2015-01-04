#! /usr/bin/python

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        # sort num first
        num.sort()
        l = len(num)
        res = []
        if l < 3:
            return []
            
        for i in range(0, l - 2):
            if i == 0 or num[i] > num[i - 1]:
                x = num[i]
                start = i + 1
                end = l - 1
                while start < end:
                    y = num[start]
                    z = num[end]
                    if x + y + z == 0:
                        res.append([x,y,z])
                        start = start + 1
                        end = end - 1
                        while start < end and num[end] == num[end + 1]:
                            end = end - 1
                        while start < end and num[start] == num[start - 1]:
                            start = start + 1
                        
                    elif x + y + z > 0:
                        end = end - 1
                    else:
                        start = start + 1
        return res
        
    
            
                    
if __name__ == "__main__":
    num = [-1 , -2 , -3, 1, 0 , 2, 5]
    sol = Solution()
    print sol.threeSum(num)
