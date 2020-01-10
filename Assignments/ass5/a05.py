class Node:
    def __init__(self, data=None):
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

    def insert( self , index , val):
        new_node = node(val)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            count += 1

        prev.next = new_node
        new_node.next = temp

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

    def reverse_list(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev    


                

           

if __name__ == '__main__': 
    l = LinkedList() 
    l.push(1) 
    l.push(2)
    l.push(3)

    print(l)

    l.reverse_list() 
    print(l)

