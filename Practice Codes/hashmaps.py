class Hashmap:
	
	def __init__(self):
		self.size = 10
		self.map = [None] * self.size

	def _get_hashed(self,key):
		if type(key) == int:
			return key % self.size
		if type(key) == str:
			return len(key) % self.size
		if type(key) == tuple:
			return len(key) % self.size

	def add(self,key,value):
		key_hash = self._get_hashed(key)
		key_value = [ key,value]

		if self.map[key_hash] is None:
			self.map[key_hash] = [key_value]
			return True

		else:
			#checkin for update ...
			for pair in self.map[key_hash]:
				if pair[0] = key:
					pair[1] = value
					return True

			self.map[key_hash].append(key_value)
			return True

	def get(self,key):
		key_hash = self._get_hashed(key)
		if self.map[key_hash] is not None:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]
		raise keyError(str(key))
		
	def delete(self,key):
		key_hash = self._get_hashed(key)
		if self.map[key_hash] is None:
			raise keyError(str(key))

		for pair in range(0,len(self.map[key_hash])):
			if self.map[key_hash][i][0] == key:
				self.map[key_hash].pop(i)
				return True	

    def __str__(self):
        ret = ""
        for i,item in enumerate(self.map):
            if item is not None:
                ret += str(i) + ":" + str(item) + "\n"
        return ret
    
    

 if __name__ == '__main__':
    h = Hashmap()

	h.add(1 , "one")
	h.add(2 , "two")
	h.add("blah" , "blah-blah")
	h.add("Hello" , "World")
	h.add(("saad","mak","been"), "bawa")

	print(h)

	h.delete(2)
	h.delete(("saad","mak","been"))
	print(h)	   																
