class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class BSTree:
    def __init__(self):
        self.root = None
    
    def insert(self,item): # at end of tree 
        newNode = Node(item)
        if not self.root:
            self.root = newNode
        else:
            # search for correct position
            ptr = self.root
            while ptr.right != None and ptr.left != None: # O(h) = O(logn)
                if item > ptr.data:
                    ptr = ptr.right
                else:
                    ptr = ptr.left
            # insert data in left or right node
            if item > ptr.data:
                ptr.right = newNode
            else:
                ptr.left = newNode
    
    def buildTree(self,data): # build a tree from list
        for item in data:
            newNode = Node(item)
            if not self.root:
                self.root = newNode
            else:
                # search for correct position
                ptr = self.root
                while ptr.right != None and ptr.left != None: # O(h) = O(logn)
                    if item > ptr.data:
                        ptr = ptr.right
                    else:
                        ptr = ptr.left
                # insert data in left or right node
                if item > ptr.data:
                    ptr.right = newNode
                else:
                    ptr.left = newNode

    def SortArrToBST(self,arr):# build a tree from sorted list
        # check if you get the last parent
        if not arr:
            return None

        mid = len(arr)//2

        root = Node(arr[mid])
        
        root.left = self.SortArrToBST(arr[:mid])
        
        root.right = self.SortArrToBST(arr[mid+1:])

        return root


tree1 = BSTree()
tree2 = BSTree()
# array Not sorted
tree1 = tree1.buildTree([2,1,4,0,2,3])
# array sorted
tree2 = tree2.SortArrToBST([0,1,2,2,3,4])
print()

    


