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
        
    def ZigZag_LR_Top(self,root):
        stk1,stk2,out = [],[],[]
        stk1.append(root)
        while(stk1 or stk2):
            while(stk1):
                temp = stk1.pop()
                out.append(temp.val)
                if(temp.right):
                    stk2.append(temp.right)
                if(temp.left):
                    stk2.append(temp.left)
                
            while(stk2):
                temp = stk2.pop()
                out.append(temp.val)
                if(temp.left):
                    stk1.append(temp.left)
                if(temp.right):
                    stk1.append(temp.right)      
        print(out,'\n')
        
    def ZigZag_RL_Top(self,root):
        stk1,stk2,out = [],[],[]
        stk1.append(root)
        while(stk1 or stk2):
            while(stk1):
                temp = stk1.pop()
                out.append(temp.val)
                if(temp.left):
                    stk2.append(temp.left)
                if(temp.right):
                    stk2.append(temp.right)
                
            while(stk2):
                temp = stk2.pop()
                out.append(temp.val)
                if(temp.right):
                    stk1.append(temp.right)
                if(temp.left):
                    stk1.append(temp.left)      
        print(out,'\n')
        
    def ZigZag_LR_Down(self,root):
        stk1,stk2,out = [],[],[]
        stk1.append(root)
        while(stk1 or stk2):
            while(stk1):
                temp = stk1.pop()
                out.insert(0,temp.val)
                if(temp.left):
                    stk2.append(temp.left)
                if(temp.right):
                    stk2.append(temp.right)
                
            while(stk2):
                temp = stk2.pop()
                out.insert(0,temp.val)
                if(temp.right):
                    stk1.append(temp.right)
                if(temp.left):
                    stk1.append(temp.left)      
        print(out,'\n')
        
    def ZigZag_RL_Down(self,root):
        stk1,stk2,out = [],[],[]
        stk1.append(root)
        while(stk1 or stk2):
            while(stk1):
                temp = stk1.pop()
                out.insert(0,temp.val)
                if(temp.right):
                    stk2.append(temp.right)
                if(temp.left):
                    stk2.append(temp.left)
                
            while(stk2):
                temp = stk2.pop()
                out.insert(0,temp.val)
                if(temp.left):
                    stk1.append(temp.left)
                if(temp.right):
                    stk1.append(temp.right)      
        print(out,'\n')    
        
bst = BST()
root = None
root = bst.insert(root, 20)
bst.insert(root, 30)
bst.insert(root, 40)
bst.insert(root, 10)
bst.insert(root, 50)
bst.insert(root, 25)

print('ZigZag TopDown Left-Right')
bst.ZigZag_LR_Top(root)

print('ZigZag TopDown Right-Left')
bst.ZigZag_RL_Top(root)

print('ZigZag DownTop Left-Right')
bst.ZigZag_LR_Down(root)

print('ZigZag DownTop Right-left')
bst.ZigZag_RL_Down(root)