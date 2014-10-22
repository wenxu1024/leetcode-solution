#! /usr/bin/python
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        return self.getnumber(s, 4)
        
    def getnumber(self,s,n):
        if n == 1:
            l = len(s)
            c = 0
            for i in range(l):
                t = int(s[i]) - int('0')
                c = 10 * c + t
            if c > 255 or c < 0 or l == 0:
                return None
            else:
                if c > 0 and s[0] == '0' or c == 0 and l > 1:
	  	    return None
		else:
		    return [s]
        else:
            shead1 = self.getnumber(s[:1], 1)
            shead2 = self.getnumber(s[:2], 1)
            shead3 = self.getnumber(s[:3], 1)
            stail1 = self.getnumber(s[1:], n - 1)
            stail2 = self.getnumber(s[2:], n - 1)
            stail3 = self.getnumber(s[3:], n - 1)
            slist = []
	    if shead1 and stail1:
                for s1 in shead1:
                    for s2 in stail1:
                        slist.append(s1 + '.' + s2)
            if shead2 and stail2:
		for s1 in shead2:
               	    for s2 in stail2:
                         slist.append(s1 + '.' + s2)
            if shead3 and stail3:
		for s1 in shead3:
               	    for s2 in stail3:
                         slist.append(s1 + '.' + s2)
            return slist
                    
        
if __name__ == '__main__':
    sol = Solution()
    slist = ['25525511135','0000','10001']
    for s in slist:
	print sol.restoreIpAddresses(s)
