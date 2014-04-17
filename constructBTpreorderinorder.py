# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if not preorder: return None
        x=preorder[0]
        i=inorder.index(x)
        leftin=inorder[:i]
        rightin=inorder[i+1:]
        leftpre=preorder[1:i+1]
        rightpre=preorder[i+1:]
        T=TreeNode(x)
        T.left=self.buildTree(leftpre,leftin)
        T.right=self.buildTree(rightpre,rightin)
        return T
        
