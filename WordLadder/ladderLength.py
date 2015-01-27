#! /usr/bin/python
import collections
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        dict = dict | set([end])
        q = collections.deque()
        visited = {}
        count = 1
        q.append((start, count)) # record both the node and its level
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for item in dict:
            visited[item] = False
        while q:
            (s, count) = q.popleft() #get the current node and its level
            if s == end:
                return count
            l = len(s)
            for i in range(l):
                for c in alphabet:
                    if c != s[i]:
                        stemp = s[:i] + c + s[i + 1:]
                        if stemp in visited and visited[stemp] == False:
                            q.append((stemp, count + 1)) # push the node and its level to the queue
                            visited[stemp] = True
        return 0
            
        

if __name__ == "__main__":
    l = ["hot", "dot", "dog", "lot", "log"]
    start = "hit"
    end = "cog"
    dict = set(l)
    sol = Solution()
    print sol.ladderLength(start, end, dict)
