class Node:

	def __init__(self, data = None ):
		self.val = data
		self.next = None

class Linkedlist:
	
	def __init__(self):
		self.head = None

	def push(self , val):
		new_node = Node(val)
		
		#no node currently
		if self.head is None:
			self.head = new_node
			return

		# otherwise reach the end and then insert
		temp = self.head
		while temp.next is not None:
			temp = temp.next

		temp.next = new_node

	def pop(self):
		
		# no node
		if self.head is None:
			raise Exception("Cannot pop...no value")

		# when one node
		if self.head.next is None:
			val = self.head.val
			self.head = None
			return val

		# when two or more nodes
		temp = self.head
		while temp.next is not None:
			prev = temp
			temp = temp.next
		val = temp.val
		prev.next = None
		return val	 

	def insert(self , index , val):
		new_node = Node(val)
		
		# at 0 index
		if index == 0:
			new_node.next = self.head
			self.head = new_node
			return

		# at any other indices
		temp = self.head
		counter = 0
		while temp is not None and counter < index:
			prev = temp
			temp = temp.next
			counter += 1
		prev.next = new_node
		new_node.next = temp	

	def remove(self,val):
		temp = self.head

		# check 1st node
		if temp is not None:
			if temp.val == val:
				self.head = temp.next
				temp = None
				return

		# for other nodes
		while temp is not None:
			
			if temp.val == val:
				break
			prev = temp
			temp = temp.next

		if temp is None:
			return

		prev.next = temp.next	


	def __str__(self):
	
		ret = "[ "
		temp = self.head
	
		while temp is not None:
			ret += str(temp.val) + " , "
			temp = temp.next
	
		ret = ret.rstrip(", ")
		ret += " ]"
	
		return ret



l = Linkedlist()
l.push(10)
l.push(20)
l.push(30)
l.insert(0,5)
l.insert(4,35)

l.remove(20)
l.remove(5)
print(l)

#l.pop()

#print(l)