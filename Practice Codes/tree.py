class TreeNode:
	
	def __init__(self,x):
		self.val = x
		self.right = None
		self.left = None

class BST(TreeNode):
	def __init__(self,val,parent=None):
		super().__init__(val):
		self.parent = parent

	def insert(self,val):
		if val < self.val:
			if self.left is None:
				new_node = BST(val , parent = self)
				self.left = new_node
			else:
				self.left.insert(val)
		else:
			if self.right is None:
				new_node = BST(val , parent = self)
				self.right = new_node
			else:
				self.right.insert(val)

	def find_root(self):
		temp = self
		while temp.parent:
			temp = temp.parent

		return temp

	def find_min(self):
		min_node = self
		if self.left:
			min_node = find_min(self.left)

		return min_node	

	def set_for_parent(self , new_ref):
		if self.parent is None: return
		if self.parent.right = self:
			self.parent.right = new_ref
		if self.parent.left = self:
			self.parent.right = new_ref

	def replace_with_node(self,node):
		self.set_for_parent(node)
		node.parent = self.parent
		self.parent = None
		return node.find_root

	def delete(self,val):
		if self.parent is None and self.left is None and self.left is None and self.val == val:
			return None
		if self.val == val:
			if self.left is None and self.right is None:
				self.set_for_parent(None)
				return self.find_root()

			if self.right is None:
				return replace_with_node(self.left)

			if self.left is None:
				return replace_with_node(self.right)

			successor = self.right.find_min()
			self.val = successor.val

			return self.right.delete(successor.val)


		if val < self.val:
			if self.left is None:
				return self.left.delete(val)
			else: return self.find_root()	

			if self.right is None:
				return self.right.delete(val)					
			else: return self.find_root()


		

b = BST(20)
b.insert(24)
b.insert(21)
b.insert(10)				 																
b.insert(25)
b.insert(26)

print(b)

b = b.delete(20)
b = b.delete(21)
b = b.delete(25)
b = b.delete(24)
b = b.delete(25)
b = b.delete(26)

print(b)


