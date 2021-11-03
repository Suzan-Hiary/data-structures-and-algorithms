class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


class AnimalShelter:
    def __init__(self):
        pass



    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
    def enqueue(self,value):
        '''
        adds a new animal with that value to the back of the queue with an O(1) Time performance.
        '''

        animal=Node(value)
        if not self.rear:
            self.front=animal
            self.rear=animal
        else:
            self.rear.next=animal
            self.rear=animal

    def is_empty(self):
        '''
        Returns: Boolean indicating whether or not the stack is empty.
        '''
        if self.front==None:
            return True
        else:
            return False
    
    def dequeue(self,pref):
        '''
        Returns: the pref animal if it was the front but if the front not equal 
        to pref it will remove it and then re add it to the queue
        then keeps doing it untill it matches the prefernce
        '''
        if not self.is_empty():
           if pref == 'dog' or pref== 'cat':
              
              while self.front.data != pref:
               
                 selectedAnimal=self.front
                 self.front=self.front.next
                 selectedAnimal.next=None
                 self.enqueue(selectedAnimal.data)
            
              selectedAnimal=self.front
              self.front=self.front.next
              selectedAnimal.next=None
              return selectedAnimal.data      
           else:
                return None
        else:
            raise Exception ('queue is empty')