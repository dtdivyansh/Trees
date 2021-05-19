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
        
    def LR_TopDown_level(self,root):
        queue = []
        temp = root
        out = []
        while(temp):
            out.append(temp.val)
            if(temp.left):
                queue.append(temp.left)
            if(temp.right):
                queue.append(temp.right)
            if(queue):
                temp = queue.pop(0)
            else:
                temp = None
        print(out,'\n')
        
    def LR_DownTop_level(self,root):
        queue = []
        temp = root
        out = []
        while(temp):
            out.insert(0,temp.val)
            if(temp.right):
                queue.append(temp.right)
            if(temp.left):
                queue.append(temp.left)
            if(queue):
                temp = queue.pop(0)
            else:
                temp = None
        print(out,'\n')
        
    def RL_DownTop_level(self,root):
        queue = []
        temp = root
        out = []
        while(temp):
            out.insert(0,temp.val)
            if(temp.left):
                queue.append(temp.left)
            if(temp.right):
                queue.append(temp.right)
            if(queue):
                temp = queue.pop(0)
            else:
                temp = None
        print(out,'\n')
        
    def RL_TopDown_level(self,root):
        queue = []
        temp = root
        out = []
        while(temp):
            out.append(temp.val)
            if(temp.right):
                queue.append(temp.right)
            if(temp.left):
                queue.append(temp.left)
            if(queue):
                temp = queue.pop(0)
            else:
                temp = None
        print(out,'\n')

bst = BST()
root = None
root = bst.insert(root, 20)
bst.insert(root, 30)
bst.insert(root, 40)
bst.insert(root, 10)
bst.insert(root, 50)
bst.insert(root, 25)

print('Top-Down Left-Right Traveersal')
bst.LR_TopDown_level(root)

print('Down-Top Left-Right Traversal')
bst.LR_DownTop_level(root)

print('Top-Down Right-Left Traversal')
bst.RL_TopDown_level(root)

print('Down-Top Right-Left Traversal')
bst.RL_DownTop_level(root)