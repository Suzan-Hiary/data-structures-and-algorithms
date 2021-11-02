
# Node class 

# Node class
class Node:

	

	def __init__(self, data):
		
		self.data = data
		self.next = None

class LinkedList:

	
	def __init__(self):
		
		self.head = None

	def isPalindrome(self, head):
		
		slow_ptr = head
		fast_ptr = head
		prev_of_slow_ptr = head
		
		# To handle odd size list
		midnode = None
		
		
		res = True
		
		if (head != None and head.next != None):
			
			
			while (fast_ptr != None and
				fast_ptr.next != None):
					
				
				fast_ptr = fast_ptr.next.next
				prev_of_slow_ptr = slow_ptr
				slow_ptr = slow_ptr.next
				
		
			if (fast_ptr != None):
				midnode = slow_ptr
				slow_ptr = slow_ptr.next
				
		
			second_half = slow_ptr
			
			
			prev_of_slow_ptr.next = None
			
			second_half = self.reverse(second_half)
			
			# Compare
			res = self.compareLists(head, second_half)
			
			
			second_half = self.reverse(second_half)
			
			if (midnode != None):
				
				prev_of_slow_ptr.next = midnode
				midnode.next = second_half
			else:
				prev_of_slow_ptr.next = second_half
		return res

	def reverse(self, second_half):
		
		prev = None
		current = second_half
		next = None
		
		while current != None:
			next = current.next
			current.next = prev
			prev = current
			current = next
			
		second_half = prev
		return second_half




# Driver code
if __name__ == '__main__':
	
	l = LinkedList()
	s = [ 'a', 'b', 'a', 'c', 'a', 'b', 'a' ]
	
	for i in range(7):
		l.push(s[i])
		l.printList()
		
		if (l.isPalindrome(l.head) != False):
			print("Is Palindrome\n")
		else:
			print("Not Palindrome\n")
		print()