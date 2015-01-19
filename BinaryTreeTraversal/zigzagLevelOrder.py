#! /usr/bin/python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    ''' Binary tree zigzag level order traversal, recursive solution'''
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        res = [[root.val]]
        resleft = self.zigzagLevelOrder(root.left)
        resright = self.zigzagLevelOrder(root.right)
        l = len(resleft)
        r = len(resright)
        t = min(l,r)
        for i in range(t):
            resright[i].reverse()
            resleft[i].reverse()
            if i % 2 == 0:
                res.append(resright[i] + resleft[i])
            else:
                res.append(resleft[i] + resright[i])
        if l < r:
            for i in range(l, r):
                resright[i].reverse()
                res.append(resright[i])
        else:
            for i in range(r, l):
                resleft[i].reverse()
                res.append(resleft[i])
        return res
        
