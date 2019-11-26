class Card:
	def __init__(self,suit,val):
		self.val = val
		self.suit = suit

	def __str__(self):
		return str(self.val) +" "+ "of" +" "+self.suit

class Deck:
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for s in ["Spades" , "Hearts" , "Diamonds" , "Clubs"]:
			for v in range(1,14):
				self.cards.append(Card(s,v))

	def __str__(self):
		ret = " "
		for c in self.cards:
			ret += str(c) + "\n"
		return ret

	
	def shuffle(self):
		import random
		for i in range(0,len(self.cards)):
			r = random.randint(0,i)
			self.cards[i],self.cards[r] = self.cards[r],self.cards[i]
	
	def draw(self):
		import random
		r = random.randint(0,len(self.cards))
		c = self.cards.pop(r)
		return c


print("\n[\]--------->Card on Diamonds , 8: \n")
c1 = Card("Diamonds" , 8)
print(c1)
print("\n")

print("[\]--------->Printing Deck of Cards: \n")
d = Deck()
print(d)										
print("\n")

print("[\]--------->Shuffling Cards:  \n")
d.shuffle()
print(d)
print("\n")


print("[\]--------->Drawing Cards: \n")
c=d.draw()
#print(c)
print(d)