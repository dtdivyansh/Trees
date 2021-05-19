class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1
        
class BST:
    # Binary Search Tree
    
    def insert(self,root,key):
        if(root==None):
            return Node(key)
        if(key<root.val):
            root.left = self.insert(root.left,key)
        else:
            root.right = self.insert(root.right,key)
            
        root.height = 1 + max( self.getHeight(root.left) , self.getHeight(root.right) )
        return root
        
    def getHeight(self,root):
        if(root==None):
            return 0
        else:
            return root.height
        
    
    def preOrder(self,root):
        if(root==None):
            return
        print(root.val,end="  ")
        self.preOrder(root.left)
        self.preOrder(root.right)
        
    def inOrder(self,root):
        if(root==None):
            return
        self.inOrder(root.left)
        print(root.val,end="  ")
        self.inOrder(root.right)
        
    def postOrder(self,root):
        if(root==None):
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val,end="  ")
        
bst = BST()
root = None
root = bst.insert(root, 10)
bst.insert(root, 30)
bst.insert(root, 40)
bst.insert(root, 20)
bst.insert(root, 50)
bst.insert(root, 25)
print('pre Order')
bst.preOrder(root)
print('\n\npost order')
bst.postOrder(root)
print('\n\nIn Order')
bst.inOrder(root)