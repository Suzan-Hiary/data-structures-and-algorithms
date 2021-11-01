from queue_with_stacks.stacks_and_queues import Stack , Node


class Pseudo_queue:
     '''
     Keep 2 stacks, let's call them head and tail you will be
     able to push to the head stack and pop from the tail stack 
     '''
     def __init__(self):
        self.head_stack=Stack()
        self.tail_stack=Stack()
        self.front=self.head_stack.top
        self.rear=self.tail_stack.top
 
     def enqueue(self,value):
         '''
          Enqueue:
           Push the new element onto head stack 
         '''
         node =  Node(value)
         node.next=self.front
         self.front=node
         self.head_stack.push(node)



     def dequeue(self):
         '''
         Dequeue:
          If tail_stack is empty, refill it by 
          popping each element from head stack and pushing it onto tail stack
          Pop and return the top element from tailstack
           Using this method, each element will be in each stack exactly once - meaning 
           each element will be pushed twice and popped twice, giving amortized constant time operations.
         '''
         if self.tail_stack.is_empty() :
            while not self.head_stack.is_empty() :
               self.tail_stack.push(self.head_stack.pop())
            
         return self.tail_stack.pop().data