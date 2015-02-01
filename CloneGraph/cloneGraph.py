#! /usr/bin/python

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        if node == None:
            return None
        # write your code here
        if node not in self.dict:
            copynode = UndirectedGraphNode(node.label)
            self.dict[node] = copynode
            for item in node.neighbors:
                if item not in self.dict:
                    copyitem = self.cloneGraph(item)
                    copynode.neighbors.append(copyitem)
                else:
                    copynode.neighbors.append(self.dict[item])
            return copynode
