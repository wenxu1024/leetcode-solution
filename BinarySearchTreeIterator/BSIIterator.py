#definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.l = []
        current = root
        while current != None:
            self.l.append(current)
            current = current.left
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.l == []:
            return False
        else:
            return True

    # @return an integer, the next smallest number
    def next(self):
        current = self.l[-1]
        self.l.pop()
        p = current
        if p.right != None:
            p = p.right
            while p != None:
                self.l.append(p)
                p = p.left
        return current.val
            
            
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
