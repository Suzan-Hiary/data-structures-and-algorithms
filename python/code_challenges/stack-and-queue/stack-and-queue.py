class Node:
   
    def __init__(self, data, next=None):
        self.data = data
        self.next= next




class Stack:
    '''this STack is implementing the (Stack data structure ) with common methods used with it'''
    top = None

    def __init__(self, top=None):
        ''' creates an empty Stack when instantiated.   '''
        self.top = top

    def push(self, value):
        '''Method, takes value as argument and adds new node with value to the top of the stack'''
        new_node = Node(value)
        new_node.next= self.top
        self.top = new_node

    def pop(self):
        '''
        Removes the node from the top of the stack
        Should raise exception when called on empty stack
        '''
        if not self.is_empty():
           removed_node=self.top
           self.top=self.top.next
           removed_node.next=None
           return removed_node.data
        else:
            raise Exception ('stack is empty')

    def peek(self):
        '''
        Returns: Value of the node located at the top of the stack
        Should raise exception when called on empty stack
        '''
        if not self.is_empty():
           return self.top.next.data
        else:
            raise Exception ('node is empty')    
        

    
    def is_empty(self):
        '''
        Returns: Boolean indicating whether or not the stack is empty.
        '''
        if self.top==None:
            return True
        else:
            return False

class Queue :
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
    def enqueue(self,value):
        '''
        adds a new node with that value to the back of the queue with an O(1) Time performance.
        '''

        node=Node(value)
        if not self.rear:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def is_empty(self):
        '''
        Returns: Boolean indicating whether or not the stack is empty.
        '''
        if self.front==None:
            return True
        else:
            return False
    
    def dequeue(self):
        '''
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue
        '''
        if not self.is_empty():
            removed_node=self.front
            self.front=self.front.next
            removed_node.next=None
            return removed_node.data
        else:
            raise Exception ('queue is empty')

    def peek(self):
        '''
        Returns: Value of the node located at the front of the queue
        Should raise exception when called on empty stack
        ''' 
        if not self.is_empty():
             return self.front
        else:
             raise Exception('queue is empty')
    # def __str__(self):
    #     return self
        



queue=Queue()
queue.enqueue(1)
print(queue)
print('a')  