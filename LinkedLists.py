class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
class LinkedList():
    def __init__(self, head = None):
        self.head = head
        
    def insertBeg(self, val):
        new = Node(val, self.head)
        self.head = new
         
    def insertEnd(self, val):
        if self.head == None:
            self.insertBeg(val)
        else:
            new = Node(val, None)
            curr = self.head
            while curr.next!= None:
                curr = curr.next
            curr.next = new
               
    def delBeg(self):
        if self.head != None:
            self.head = self.head.next
        else:
            print("Already empty\n")
          
    def delEnd(self):
        if self.head == None:
            print("Already empty\n")
        elif self.head.next == None:
            self.head = None
        else:
            curr = self.head
            while curr.next.next != None:
                curr = curr.next
            curr.next = None
            
    def insertAfter(self, num, val):
        if self.head == None:
            print("Number not found\n")
        else:
            curr = self.head
            while curr!=None and curr.data!=num:
                curr = curr.next
            if curr!= None:
                new = Node(val, curr.next)
                curr.next = new
            else:
                print("Number not found\n")

    def insertBefore(self, num, val):
        if self.head == None:
            print("Number not found\n")
        else:
            curr = self.head
            while curr.next!=None and curr.next.data!=num:
                curr = curr.next
            if curr.next!= None:
                new = Node(val, curr.next)
                curr.next = new
            else:
                print("Number not found\n")
             
    def delete(self, num):
        if self.head == None:
            print("Number not found\n")
        else:
            curr = self.head
            while curr.next!=None and curr.next.data!=num:
                curr = curr.next
            if curr.next!= None:
                curr.next = curr.next.next
            else:
                print("Number not found\n")

    def disp(self):
        if self.head == None:
            print("Empty")
        else:
            curr = self.head
            while(curr!=None):
                print(curr.data, end = "->")
                curr = curr.next  
            print("NULL\n")
          
if __name__ == "__main__":
    ll = LinkedList()
    number = 0
    while(number < 9):
        print("1. Add to beginning")
        print("2. Add to end")
        print("3. Delete from beginning")
        print("4. Delete from end")
        print("5. Add after this")
        print("6. Add before this")
        print("7. Delete this")
        print("8. Display")
        print("9. Exit")
        
        number = int(input("Enter choice: "))
        
        if number == 1:
            val = int(input("Enter number to insert: "))
            ll.insertBeg(val)
        
        if number == 2:
            val = int(input("Enter number to insert: "))
            ll.insertEnd(val)
        
        if number == 3:
            ll.delBeg()
        
        if number == 4:
            ll.delEnd()
            
        if number == 5:
            num = int(input("Enter number after which to insert: "))
            val = int(input("Enter number to insert: "))
            ll.insertAfter(num, val)
            
        if number == 6:
            num = int(input("Enter number before which to insert: "))
            val = int(input("Enter number to insert: "))
            ll.insertBefore(num, val)
        
        if number == 7:
            num = int(input("Enter number to delete: "))
            ll.delete(num)    
        
        if number == 8:
            ll.disp()