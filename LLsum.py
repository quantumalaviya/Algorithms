from LinkedLists import *

def sum(head1, head2, carry = 0):
    if not head1 and not head2 and carry:
        return Node(carry)
    elif head1 and not head2:
        s = head1.data + carry 
        return Node(s%10, sum(head1.next, None, s//10))
    elif head2 and not head1:
        s = head2.data + carry 
        return Node(s%10, sum(None, head2.next, s//10))
    elif head1 and head2:
        s = head1.data + carry + head2.data
        return Node(s%10, sum(head1.next, head2.next, s//10))
    
    
head1 = LinkedList()
head1.insertBeg(6)
head1.insertBeg(1)
head1.insertBeg(7)

head2 = LinkedList()
head2.insertBeg(2)
head2.insertBeg(9)

x = sum(head1.head, head2.head)
x = LinkedList(x)
x.disp()