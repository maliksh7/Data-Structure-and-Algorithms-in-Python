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
            print ("Push case 1")
            new_node.next = self.head
            return 

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        print ("pushed? case 2")
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
        print("Insertion Case 2")
        new_node.next = temp


    def __str__(self):
        ret = "["
        temp = self.head

        while temp is not None:
            print ("Executing! ")
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
            
        if self.head.next is None:
            val = self.head.val
            self.head = None
            return val


        last = self.get_last()
        print (last)
        while temp != last:
            temp = temp.next

        temp.next = self.head
        last.next = None

        return


    
    def remove(self, val):
        if self.head is None:
            raise Exception("The list is empty")

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

        while temp != last:
            temp = temp.next
            counter += 1

        counter += 1
        return counter 

    def rev_list(self):
        temp = self.head
        last = self.get_last()
        new_node = last
        processing = new_node

        if self.head is None: return
        if self.head.next is None: return

        for i in range(self.len()-1):
            while temp.next != processing:
                temp= temp.next

            processing.next = temp
            processing = temp
            
        self.head.next = None
        self.head = new_node
            


            


list = Ring()
list.push(1)
list.push(2)
list.push(3)

print (list)
list.rev_list()





print (list)

# list.remove(12)
# print (list)
