class Node:
	def __init__(self,val=None):
		self.val = val
		self.next = None

class SLL:

	def __init__(self):
		self.head = None

	def push(self,val):

		#1. When there are no nodes
		#2. When there is already one or more nodes

		new_node = Node(val)
		if self.head is None:        #chk whether head is None
			self.head = new_node     #insert newnode on head
			return

		last = self.head
		while last.next is not None:    #reach the end
			last = last.next
		last.next = new_node          #insert 
		
	def pop(self):

		#1. When there is no nodes
		#2. When there are 2 are more nodes-- in this case we keep two pointer: prev and temp.
		#Move both untill temp is the last.Then set next of prev to None 

		# no node
		if self.head is None:
			raise Exception("No value to pop....!")

		# Only one node
		if self.head.next is None:
			val = self.head.val
			self.head = None
			return val

		# two or more nodes
		temp = self.head
		while temp.next is not None:
			prev = temp
			temp = temp.next

		val = temp.val
		prev.next = None
		return val

	def __str__(self):

		ret = "["
		temp = self.head
		while temp is not None:
			ret += str(temp.val) + ", "		
			temp = temp.next

		ret = ret.rstrip(', ')
		ret += "]"
		return ret	

	def insert(self,index,val):
		new_node = Node(val)

		#1. Insertion at index 0: new head, old head becomes next of this new head
		#2. Insertion at any index: in this case move prev and temp forward index times.
		#Then,insert new node between prev and temp

		# Case 1:
		if index == 0:
			print("Case 1: ")
			new_node.next = self.head
			self.head = new_node
			return

		temp = self.head
		counter = 0

		# Case 2:
		print("Case 2: ")
		while temp and counter < index:
			prev = temp
			temp = temp.next
			counter += 1

		prev.next = new_node
		new_node.next = temp

	def remove(self,val):
		#1. If first node is present and same as val, remove it.
		#2. Otherwise,move prev and temp until temp points to the value.
		#Set next of prev to next of temp	
		temp = self.head
		if temp is not None:
			if temp.val == val:
				print("Case 1: ")
				self.head = temp.next
				temp = None   #Not needed, really!!
				return

		while temp is not None:
			if temp.val == val:
				break

			prev = temp
			temp = temp.next

		if temp is None:
			print("Case 2.1")
			return

		print("Case 2.2")
		prev.next = temp.next  #just lose th reference to delete node

	def len(self):

		temp = self.head
		counter = 0
		while temp:
			temp = temp.next
			counter += 1
		return counter
		
	def get(self,index):

		temp = self.head
		counter = 0
		while temp:
			if index > self.len() - 1:
				raise IndexError("Index Out of Range..!")
			if counter == index:
				return temp.val
			temp = temp.next
			counter += 1	 	

				 
							






if __name__ == "__main__": 
    l = SLL() 
    l.push(5) 
    l.push(6) 
    l.push(7)
    l.pop()

    l.insert(0,0)
    l.insert(3,8)
    l.remove(6)

    print(l)

    print(l.len())

    print(l.pop()) 
    
    print(l.len())

    print(l.get(0))
    print(l)
    l.get(2) # Should say "IndexError: Index out of bound"



