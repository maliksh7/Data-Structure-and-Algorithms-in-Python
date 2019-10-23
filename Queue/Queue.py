class Queue:
	def __init__(self):
		self.size = 5
		self.q = list(range(self.size))
		self.i = 0
		self.out = 0

		self.is_empty = True
		self.is_full = False

	def _inc(self , index):
		if index + 1 == self.size:
			return 0

		else:
			return index + 1

	def enqueue(self , val):
		if self.is_full:
			raise IndexError("Queue full....Cannot enqueue.")
		self.q[self.i] = val
		self.i = self._inc(self.i)				
		
		if self.i == self.out:
			self.is_full = True
		self.is_empty = False
		
	def dequeue(self):
		if self.is_empty:
			raise IndexError("Queue empty...Cannot dequeue")

		ret = self.q[self.out]
		self.out = self._inc(self.out)			

		if self.out == self.i:
			self.is_empty = True
		self.is_full = False																					
		
		return ret

	def __str__(self):
		return str(self.q) + ", in: " + str(self.i) + ", out: " + str(self.out)		


q = Queue()
#q = _inc(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print(q)

q.dequeue()
q.dequeue()

print(q)
