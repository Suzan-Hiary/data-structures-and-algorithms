class Node :
    def __init__(self , data ) :
        self.data = data
        self.left = None
        self.right=None
        


class BinaryTree :
    def _init__(self ):
        self.root = None
        


    def pre_order(self ):
        """ a method to traverse the Binary tree in a pre_order order 
        Args : root 
        return : root -->left subtree  --> right subtree"""
        result =[]
        node =  self.root
        result.append(node.data)
        if node.left :

            self.pre_order(node.left , result)
            
        
        if node.right :

            self.pre_order(node.right, result)

        return result


    def post_order(self  ):
        result=[]
        node = self.root

        if node.left :
            self.post_order(node.left , result)
        
        
        if node.right:
            self.post_order(node.right , result)

        result.append(node.data)
        return result 

    def in_order(self  ):
        result=[]
        node = self.root

        if node.left :
            self.in_order(node.left , result)
        
        result.append(node.data)

        if node.right:
            self.in_order(node.right , result)

        
        return result

class Binary_Search_Tree :

    def __init__(self , data=None):
        super().__init__(data)

    
    def add(self , value):
        node = Node(value)

        if not self.root :
            self.root = node

            return 

        current = self.root 

        while True :
            if node.data < current.data:
                if current.left :
                   current = current.left

                else : 
                    current.left = node 
                    return 

            else: 
                if current.right :
                    current = current.right   
                else :
                    current.right = node 
                    return




    
    def contains (self , value ):

       

        if not self.root :
            return False

        current = self.root

        while True :

            if  value == current.data:

                return True

            if value < current.data :
                if current.left :
                    current = current.left

                else :
                     return False
            else:
                if current.right :
                    current= current.right

                else :
                    return False









tree = Binary_Search_Tree()
tree.add(66)
tree.add(60)
tree.add(55)
tree.add(50)
tree.add(40)
print(tree)


