# Create Data Stractures
class Node:
    # Define Constractor Function
    def __init__(self,data) -> int:
        self.data = data
        self.next = None
class LinkedQueue:
    # Define Constractor Function
    def __init__(self):
        self.queue = None
    
    # Define Enqueue Function (To Put New Element)
    def enqueue(self,item):
        newNode = Node(item)
        
        # Check if queue is empty
        if self.queue is None:
            self.queue = newNode
        
        # Queue not empty
        else:
            temp = self.queue
            while temp.next:
                temp = temp.next
            temp.next = newNode
    
    # Define Dequeue Function (To Delete First Element)
    def dequeue(self):
        if self.queue is not None:
            temp = self.queue
            self.queue = self.queue.next 
            temp = None 

    # To get Front Of Queue
    def getFrontData(self):
        data = self.queue.data
        return data
class OrderedQueue(LinkedQueue):
    # Define Constractor
    def __init__(self):
        self.queue = None
    
    # Override Enqueue Function
    def enqueue(self, item):
        newNode = Node(item)
        # if queue is empty
        if self.queue is None:
            self.queue = newNode
        
        # if queue is not empty
        else:
            temp = self.queue
            
            # if New Element > the first element in Queue      
            if item > temp.data:
                # To point to correct position in Ordered Queue
                while temp.next and item > temp.next.data:
                    temp = temp.next
                
                # insert new item in the correct position
                newNode.next = temp.next
                temp.next = newNode
            
            # if New Element <= the first element in Queue            
            else:
                # insert new item in front
                newNode.next = temp
                self.queue = newNode
    
    # Get Minimum Element in Ordared Queue
    def getMini(self):
        data = self.queue.data
        return data


# Initilize 3 Queues
waitQ        = LinkedQueue()
WaitAndServQ = LinkedQueue()
OrderedQ     = OrderedQueue()

# Read Configuration File
file = "G:\\MeMe\\Programming\\data.ini" ### change Path in your pc
config = open(file,"r")

# take all data from file
lines = list(config.readlines())
numOfTellers = int(lines[0][11:-1])
counter = 0

# Build 3 LinkedQueues
for i in range(1,len(lines)):
    # Take Arrival Time & Service Time line by line
    arrival = int(lines[i][8:-12])
    service = int(lines[i][19:-1])

    # Check If tellers is NOT busy 
    if counter < numOfTellers:
        waitQ.enqueue(0)
        WaitAndServQ.enqueue(service)
        OrderedQ.enqueue(arrival + service)
        counter += 1
    
    # Check If tellers is busy
    else:
        OldCustTime = OrderedQ.getMini()
        
        # Check if old customer has NOT gone To new customer wait him
        if OldCustTime > arrival:
            wait = (OldCustTime - arrival) # Waiting Time
            waitQ.enqueue(wait)
            WaitAndServQ.enqueue(wait + service)
            OrderedQ.enqueue(OldCustTime + service)
            OrderedQ.dequeue()
        
        # Check if old customer has gone To new customer take his position
        else:
            waitQ.enqueue(0)
            WaitAndServQ.enqueue(service)
            OrderedQ.enqueue(arrival + service)
            OrderedQ.dequeue()


# Display Results
for _ in range(1,len(lines)):
    print(f"wait: {waitQ.getFrontData()} waitandservice {WaitAndServQ.getFrontData()}")
    waitQ.dequeue()
    WaitAndServQ.dequeue()

# Close File
config.close()


