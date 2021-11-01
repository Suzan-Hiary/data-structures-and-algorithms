class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



class BinaryTree():

    def __init__(self):
        self.root=None

    def pre_order(self):
      """
    A binary tree method which returns a list of items that it contains in (pre order) 
       root >> left >> right
    input: None
    output: tree items(list)
    we used the function (recur) to help with recursion inside the class
      """
      order=[]
      def recur(node):
          if node:
              order.append(node.data)
              if node.left:
                  recur(node.left)
              if node.right:
                  recur(node.right)    
      recur(self.root) 
      return order 


    def in_order(self):
      """
    A binary tree method which returns a list of items that it contains in (in order) 
       left >> root >> right
    input: None
    output: tree items(list)
    we used the function (recur) to help with recursion inside the class
      """
      order=[]
      def recur(node):
          if node:
              if node.left:
                  recur(node.left)
              order.append(node.data)
              if node.right:
                  recur(node.right)    
      recur(self.root) 
      return order      
    def post_order(self):
      """
    A binary tree method which returns a list of items that it contains in (post order) 
           left >> right >> root
    input: None
    output: tree items(list)
    we used the function (recur) to help with recursion inside the class
      """
      order=[]
      def recur(node):
          if node:
              if node.left:
                  recur(node.left)
              if node.right:
                  recur(node.right)   
              order.append(node.data) 
      recur(self.root) 
      return order     


    def maximum(self):
          '''
          Find the maximum value stored in the tree. 
          Arguments: none
          Returns: number
          '''
          arr=self.pre_order()
          max_val=self.root.data
          for i in arr:
              if int(i) > max_val:
                  max_val=int(i)
          return max_val




class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)




class BinarySearchTree(BinaryTree):
    
    def add(self,value):
        if not self.root:
            self.root= Node(value)
        else :
            temp = self.root
            while temp:
                if value < temp.data:
                    if not temp.left:
                        temp.left = Node(value)
                        break
                    temp = temp.left
                else:
                    if not temp.right:
                        temp.right = Node(value)
                        break
                    temp = temp.right
        pass

    def __contains__(self,value):
        """
        search for a value in the tree
        input : value
        output : True/False
        """
        if not self.root:
            raise Exception("Empty Tree !!!")

        else:
            temp = self.root
            while temp:
                if temp.data == value:
                    return True
                elif temp.data > value:
                    if not temp.left:
                        return False
                    temp = temp.left
                else:
                    if not temp.right:
                        return False
                    temp = temp.right



if __name__=='__main__':

  bt= BinarySearchTree()
  bt.add(5)      
  bt.add(3)
  bt.add(6)
  bt.add(4)
  bt.add(1)
  bt.add(2)
  print(bt.pre_order()) 