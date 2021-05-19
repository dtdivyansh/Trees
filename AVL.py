class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1
        
class AVL:
    # Binary Search Tree
    
    def insert(self,root,key):
        if(root==None):
            return Node(key)
        if(key<root.val):
            root.left = self.insert(root.left,key)
        else:
            root.right = self.insert(root.right,key)
            
        root.height = 1 + max( self.getHeight(root.left) , self.getHeight(root.right) )
        
        balance = self.getBalance(root)
        
        if(balance>1 and root.left and key<root.left.val): # Left-Left Case
            return self.rightRotate(root)
        
        if(balance>1 and root.left and key>=root.left.val): # Left-right Case
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if(balance<-1 and root.right and key>root.right.val): # Right-Right Case
            return self.leftRotate(root)
            
        if(balance<-1 and root.right and key<=root.right.val): # Right-Left Case
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)    
        return root
    
    def rightRotate(self,ro):
        temp = ro.left
        temp2 = temp.right
        temp.right = ro
        ro.left = temp2
        
        ro.height = 1 + max(self.getHeight(ro.left), self.getHeight(ro.right))
        temp.height = 1 + max( self.getHeight(temp.left), self.getHeight(temp.right) )
        return temp
    
    def leftRotate(self,ro):
        temp = ro.right
        temp2 = temp.left
        temp.left = ro
        ro.right = temp2
        
        ro.height = 1 + max(self.getHeight(ro.left), self.getHeight(ro.right))
        temp.height = 1 + max( self.getHeight(temp.left), self.getHeight(temp.right) )
        return temp
        
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
        
    def getBalance(self,root):
        if(not root):
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def levelOrder(self,root):
        queue = []
        temp = root
        while(temp):
            print(temp.val,end='  ')
            if(temp.left):
                queue.append(temp.left)
            if(temp.right):
                queue.append(temp.right)
            if(queue):
                temp = queue.pop(0)
            else:
                temp = None
                
    def maxDepth(self,root):
        print(root.height)
            

avl = AVL()
root = None
root = avl.insert(root, 10)
root = avl.insert(root, 20)
root = avl.insert(root, 30)
root = avl.insert(root, 40)
root = avl.insert(root, 50)
root = avl.insert(root, 25)

print('Pre Order')
avl.preOrder(root)
print('\n\nLevel Order')
avl.levelOrder(root)