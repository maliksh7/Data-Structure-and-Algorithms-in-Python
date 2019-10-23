




class Node:
    def __init__(self , data = None):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self , val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node
            return

        last = self.head     
        while last.next is not None:
            last = last.next

        last.next = new_node 

    def pop(self):
        if self.head == None:
            raise Exception ("Cannot pop , as no value")

        if self.head.next is None:
            val = self.head.val
            self.head = None
            return val          

        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next

        val = temp.val
        prev.next = None
        return val    

    def __str__(self):
        ret_str = "["
        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ", "
            temp = temp.next

        ret_str = ret_str.rstrip(', ')
        ret_str += "]"
        return ret_str

    def len(self):

        count = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            count += 1
        return count  

    def remove(self , val):
        temp = self.head
        if temp is not None:
            if temp.val == val:
                self.head = temp.next
                temp = None
                return    

        while temp is not None:
            if temp.val == val:
                break
            prev = temp
            temp = temp.next                 
        if temp is None:
            return

        prev.next = temp.next 
        
    def get(self , index):
        temp = self.head
        counter = 0
        
        while (temp):
            if index > self.len() - 1:
                raise IndexError("Index out of bound")
            if counter == index:
                return temp.val
            counter += 1
            temp = temp.next 

            temp.next = temp.next.next
    def remove_at(self, index):
        temp = self.head
        if temp is None and index >= 0:
            return

        if self.len() == 1 and index == 0:
            self.head = None
        else:
            count = 0
            while (count+1) != index:
                print("->",temp.val)
                temp = temp.next
                count += 1
            temp.next = temp.next.next

    def min(self):
        if self.head is None: return None

        l_min = self.head.val
        temp = self.head.next

        while temp is not None:
            if temp.val < l_min:
                l_min = temp.val

            temp = temp.next
        return l_min

    def max(self):
        if self.head is None: return None
        l_max_i = 0
        l_max = self.head.val
        temp = self.head.next
        counter = 1
        while temp is not None:
            if temp.val > l_max:
                l_max =temp.val
                l_max_i = counter
            temp = temp.next
            counter+=1
        return l_max,l_max_i

    def find_three_least(self,l):
    	if len(l) < 3: return None

    	h1 = l[0]
    	h2 = l[0]
    	h3 = l[0]

    	for i in l:
    		if i <= h1:
    			h3 = h2
    			h2 = h1
    			h1 = i
    		if i <= h2:
    			h3 = h2
    			h2 = i
    		if i <= h1:
    			h1 = i
    	return (h1,h2,h3)

    def find_three_least(l):
    	return find_three_least(l)[2]				


    def remove_max(self):
    	if self.head is None: return
    	l_max_i = self.max()[0]

    	self.remove_at(l_max_i)                        
 
if __name__ == "__main__": 
    l = LinkedList() 
    l.push(5) 
    l.push(6)
    l.push(96) 
    l.push(36)
    l.push(66)
    print("Minimum in Linkedlist is: " , l.min())
    print("Maximum in Linkedlist is: " , l.max())

    print(l)
    p = [1,2,3,4,78,56,34]
    l.find_three_least(p)
    # l.remove_max()
    print(l)
    # print(l.get(0))
    # l.get(2) # Should say "IndexError: Index out of bound"

