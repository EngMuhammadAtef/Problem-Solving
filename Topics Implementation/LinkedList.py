class Node:
    def __init__(self,Data) -> str:
        self.data = Data
        self.next = None # ptr
class SinglyLinkedList:
    def __init__(self):
        self.head = None # ptr to first
        self.last = None # ptr to last
        self.length = 0
    def insertlast(self,item:int):
        newNode = Node(item)
        self.length += 1
        if self.head == None:
            self.head = self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
    
    def insertfirst(self,item:int):
        newNode = Node(item)
        self.length += 1
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
            

    def getLength(self):
        return self.length


    def printLinkedList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
            


sll =  SinglyLinkedList()
n = int(input())

for _ in range(n):
    item = int(input())
    sll.insertlast(item)
sll.printLinkedList()

