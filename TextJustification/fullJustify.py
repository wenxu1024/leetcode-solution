#! /usr/bin/python

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L): 
        linelist = self.partition(words, L)
        stringlist = []
        n = len(linelist)
        for i in range(n - 1):
            stringlist.append(self.concatenate(linelist[i], L, False))
        stringlist.append(self.concatenate(linelist[n - 1], L, True))
        return stringlist

    
    def partition(self, words, L): 
        n = len(words)
        c = 0 
        line = []
        linelist =[] 
        for i in range(n):
            c += (len(words[i]) + 1)
            line.append(words[i])
            if c - 1 > L:
                word = line.pop()
                linelist.append(line)
                c = len(word) + 1
                line = [word]
        linelist.append(line)
        return linelist

    def concatenate(self, line, L, lastline):
        if lastline:
            n = len(line)
            sline = ""
            for i in range(n - 1):
                sline += (line[i] + " ")
            sline += line[n - 1]
            ln = self.linelen(line)
            hole = L - ln
            return sline + hole * " "

        ln = self.linelen(line)
        hole = L - ln
        n = len(line)
        if n == 1:
            sline = line[0] + hole * " " 
            return sline
        avehole = hole / (n - 1) 
        remainder = hole - (n - 1) * avehole
        if remainder == 0:
            sline = ""
            for i in range(n - 1): 
                sline += (line[i] + avehole * " " + " ")
            sline += line[n - 1]
            return sline  
        else:
            sline = ""
            for i in range(n - 1):
                if i < remainder:
                     sline += (line[i] + avehole * " " + " " + " ")
                else:
                     sline += (line[i] + avehole * " " + " ")
            sline += line[n - 1]
            return sline



    def linelen(self,line):
        l = 0
        n = len(line)
        for s in line:
            l += len(s)
        return l + n - 1 
            

if __name__ == "__main__":
    sol = Solution()
    words = ["Here", "is", "an", "example", "of", "text", "justification."]
    L = 14
    justified = sol.fullJustify(words, L)
    for line in justified:
       print line

