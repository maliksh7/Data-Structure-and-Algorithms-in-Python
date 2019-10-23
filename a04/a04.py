class Node:
    def __init__(self, val = None):
    	self.val = val 
    	self.next = None

class Ring:
    def __init__(self):
    	self.head = None

    def push(self , val):

        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return 

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head
        return 

    
    def get_last(self):
        if self.head is None:
            return None

        last =self.head.next
        while last.next != self.head:
            last = last.next
        
        print (last)
        return last

    def insert(self,index, val):
        new_node = Node(val)
        last = self.get_last()


        #Inserting at zeroth index
        if index == 0:
            new_node.next = self.head
            self.head = new_node

            if last is None:
                self.head.next = self.head

            else:
                last.next = new_node

            return

        #Inserting at Indices greater than zero
        temp = self.head
        counter = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1

        prev.next = new_node
        new_node.next = temp


    def __str__(self):
        ret = "["
        temp = self.head

        while temp is not None:
            ret += str(temp.val) + ','
            temp = temp.next

            if temp == self.head:
                break
        ret = ret.rstrip(',')
        ret += "]"

        return ret


    def pop(self):
        temp = self.head
        if self.head is None:
            raise Exception("The list is empty")
            
        if self.head.next == self.head:
            val = self.head.val
            self.head = None
            return 

        ### there is something in the list

        prev = temp
        while temp.next != self.head:
        	prev = temp
        	temp = temp.next
        	
        if prev == self.head:
        	prev.next = self.head
        else:
        	prev.next = self.head 
        return


        # last = self.get_last()
        # print (last)
        # while temp != last:
        #     temp = temp.next

        # temp.next = self.head
        # last.next = None

        # return


    #Remove 
    def remove(self, val):
        if self.head is None:
            raise Exception("The  is empty")

        temp = self.head
        last = self.get_last()

        if temp.val == val:
            if last == self.head:
                self.head = None

            else:
                self.head = temp.next
                last.next = self.head
            return

        prev = temp 
        temp = temp.next

        while temp != self.head:
            if temp.val == val:
                break

            prev = temp 
            temp = temp.next

        if temp == self.head:
            return 

        prev.next = temp.next


    def len(self):
        counter = 0
        temp = self.head
        last = self.get_last()

        if temp == None:
        	return 0

        while temp != last:
            temp = temp.next
            counter += 1

        counter += 1
        return counter 

    def get(self, index):
        counter = 0
        temp = self.head
        if self.head is None:
            raise IndexError

        while counter < index:
            temp = temp.next
            counter += 1
        
        return temp.val
    
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


if __name__ == '__main__': 
    r = Ring()
    # r.insert(1, 1)
    #r.insert(0, 1)
    #r.insert(0, 2)
    #r.insert(1, 3)
    #r.insert(7, 5)  # different behavrior since it's a ring! 
    r.push(5)
    #r.push(8)
    #r.push(12)
    print(r.len())
    print(r)
    r.remove_at(0)
    print(r)
    print(r.get(1))
