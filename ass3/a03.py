




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
 #   def insert
if __name__ == "__main__": 
    l = LinkedList() 
    l.push(5) 
    l.push(6) 

    print(l)

    print(l.len())

    print(l.pop()) 
    
    print(l.len())

    print(l.get(0))
    l.get(2) # Should say "IndexError: Index out of bound"

