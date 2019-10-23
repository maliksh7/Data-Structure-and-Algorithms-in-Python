##
##  Doubly linked List in Python 
## M Saad Hassan P17-6137


class Node(object):

    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


class Dll(object):

    def __init__(self):
        self.head = None

    
    def append(self,x):
    
        if self.head == None:
            self.head = Node(x,None, None)
            
            print ("Added to Head")

        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
        
            temp = Node(x,cur,None)
            cur.next = temp
            print ("Added")
            


    def __str__(self):
        # listt = []
        cur = self.head
        # self.head.prev = cur
        ret = "["

        while cur is not None:
            ret += str(cur.val) + ","
            # print (cur.val, "This is the previous val")
            # print (cur.val)
            cur = cur.next

        ret = ret.rstrip(",")
        ret += "]"

        # print (ret)
        return ret
            
        

    def len(self):
        counter = 0
        temp = self.head
        last = self.get_last()

        while temp != last:
            temp = temp.next
            counter += 1

        counter += 1
        return counter

    def get_last(self):
        if self.head is None:
            return None

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        return temp
        
        # print (last)
        # return last

    def rev_doubly(self):

        new_head = None
        temp = self.head 
          
        # Swap next and prev for all nodes of  
        # doubly linked list 
        while temp is not None:
            new_head , temp.prev = temp.prev , temp.next 
            #temp.prev = temp.next
            temp.next = new_head
            temp = temp.prev
  
        # Before changing head, check for the cases like  
        # empty list and list with only one node 
        if new_head is not None: 
            self.head = new_head.prev 



var = Dll()

print(var)
var.rev_doubly()
print(var)

