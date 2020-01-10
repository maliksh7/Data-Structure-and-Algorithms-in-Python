class HashMap:

	def __init__(self):
		self.size = 10
		self.map = [None] * self.size
		
	def _get_hash(self, key):
		if type(key) == int:
			return key % 10
		if type(key) == str:
			return len(key) % 10
		if type(key) == tuple:
			return len(key) % 10

	def add(self, key, value):
		hashed_key = self._get_hash(key)
		hashed_val = [key, value]
		if self.map[hashed_key] is None:	
			self.map[hashed_key] = [hashed_val]
			return True
		else:
			for pair in self.map[hashed_key]:
				if pair[0] == key:
					pair[1] = value
					return

		self.map[hashed_key].append(hashed_val)
		return True

	def get(self, key):
		hashed_key = self._get_hash(key)
		if self.map[hashed_key] is not None:
			for pair in self.map[hashed_key]:
				#print("[Note]", type(pair) , pair)
				if pair[0] == key:
					return pair[1]
		raise KeyError(str(key))

	def __str__(self):
		ret = " "
		for i, item in enumerate(self.map):
			if item is not None:
				ret += str(i) + ":" + str(item) + "\n"
		return ret	 	 

	def delete(self,key):
		hashed_key = self._get_hash(key)

		if self.map[hashed_key] is None:
			raise KeyError(str(key))

		for i in range(0,len(self.map[hashed_key])):
			if self.map[hashed_key][i][0] == key:
				self.map[hashed_key].pop(i)
				return True	

		raise KeyError(str(key))

    


if __name__ == '__main__': 
    h = HashMap() 

    h.add(17, "seventeen")
    h.add(26, "twenty six")
    h.add(35, "thirty five")
    h.add(25, "twenty five")
    h.add(26, "twenty six updated")
    h.add(887, "large number")

    print(h)

    print("[NOTE] Running Test on String type keys ...")

    h.add("Saad", "Hassan")
    h.add("Saad", "Mubeen")
    h.add("MAK", "Mubariz")
    print(h)

    print("[NOTE] Running Test on Tuple type keys ...")

    h.add(("saad","mak","been"), "bawa")
    print(h)


    print(h.get(17))
    print(h.get("Saad"))
    print(h.get("MAK"))
    print(h.get(("saad", "mak", "been")))


    print("[NOTE] Running Test on Deletion of Keys ...")

    print(h.delete(17))
    print(h.delete("MAK"))
    print(h.delete(("saad", "mak", "been")))

    
    print(h)