#! /usr/bin/python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        root.next = None
        if root.left == None and root.right == None:
            return
        elif root.left != None and root.right == None:
            self.connect(root.left)
            return
        elif root.left == None and root.right != None:
            self.connect(root.right)
            return
        else:
            self.connect(root.left)
            self.connect(root.right)
            leftmostleft = root.left
            leftmostright = root.right
            while leftmostleft and leftmostright:
                linkleft = leftmostleft
                while linkleft.next:                   # get the tail of the leftmost linked list
                    linkleft = linkleft.next
            
                while leftmostleft:  # update leftmost listnode to the next level in the left subtree
                    if leftmostleft.left:
                        leftmostleft = leftmostleft.left
                        break
                    else:
                        if leftmostleft.right:
                            leftmostleft = leftmostleft.right
                            break
                        else:
                            leftmostleft = leftmostleft.next
                linkleft.next = leftmostright # link the tail of the current level to the leftmost listnode of right subtree
                while leftmostright: # update the leftmost listnode of the next level in the right subtree
                    if leftmostright.left:
                        leftmostright = leftmostright.left
                        break
                    else:
                        if leftmostright.right:
                            leftmostright = leftmostright.right
                            break
                        else:
                            leftmostright = leftmostright.next
                
