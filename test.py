# from typing import Counter


# class Node :
#     """ method to create a new Node"""

#     def __init__(self , data , next = None):
#         self.data = data
#         self.next = next 


# class LinkedList:

#     def __init__(self):
#         self.head =None


#     def insert(self , value):
#         self.head = Node(value,self.head)
#         return self.head
    
#     def append(self , value):
#         currentnode = self.head
#         while currentnode != None:
#             if currentnode.next is None :
#                   currentnode.next = Node(value)
#                   break
#             currentnode = currentnode.next
    
#     def __str__(self):
        
#         string = ""
#         currentnode=self.head

#         while currentnode != None:
#             value = currentnode.data
#             if currentnode.next is None:
#                 string += "{" + f'{value}' + '}' + "-> Null"
#                 break
                
#             else:
#                 string += "{" + f'{value}' + '}' + "-> "
#                 currentnode = currentnode.next
#         return string       
        
                   
#     def multi_append(self , list):
#         """method takes an array as a args and append the list to the end of the list"""

#         for i in list:
#             self.append(i)
#         return
    
#     def insertbefore(self , target , value):
#         """ method takes the value and the target value and return the value inserted before the target value"""

#         newnode = Node(value)
#         current = self.head
        
#         if current != None:
#             while current:
                
#                 if current.next.data == target:
#                     newnode.next = current.next
#                     current.next = newnode
#                     break
#                 else:
#                     current = current.next
                    

#     def insertafter(self,target ,value):

#         newnode = Node(value)
#         currentnode=self.head

#         if currentnode != None:
#             while currentnode:
#                 if currentnode.data == target :
#                     newnode.next = currentnode.next
#                     currentnode.next = newnode
#                     break
#                 else:
#                     currentnode = currentnode.next


#     def zip(list1 , list2):

     




# ll=LinkedList()
# ll.insert(1)
# ll.insert(2) 
# ll.insert(3) 

# ll.insert(5)
# ll.append(4)
# print(ll.insertbefore(1,99))
# print(ll.insertafter(1,99))
# # ll.multi_append([4,5,6,7])
# print(ll)
