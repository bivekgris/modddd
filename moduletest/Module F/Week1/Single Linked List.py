from turtle import position


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def prepend(self,data):
        new_node=Node(data)
        
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        
    
    def append(self,data):
        new_node=Node(data)
        
        if self.head==None:
            self.head=new_node
        
        else:
            #traversing the linked list to find the last node
            curr=self.head
            while curr.next!=None:
                curr=curr.next #this is the last node
            curr.next=new_node #point the next element of the last node to the newly created node
            
    def insert(self,data,position):
        new_node=Node(data)
        
        curr_node=self.head
        prev=None
        count=0
        while curr_node!=None and count<position:
            prev=curr_node
            curr_node=curr_node.next
            count+=1
            
        if curr_node!=self.head:
            prev.next=new_node
            new_node.next=curr_node
        else:
            new_node.next=curr_node
            self.head=new_node
            
    def traverse(self):
        curr_node=self.head
        my_elements=[]
        while curr_node!=None:
            my_elements.append(curr_node.data)
            curr_node=curr_node.next
        return my_elements
            
    def delete_first(self):
        if self.head==None:
            print('Empty Linked List')
        else:
            curr_node=self.head
            self.head=self.head.next
            del curr_node
            
    def delete_last(self):
        if self.head==None:
            print('Empty Linked List')
        else:
            curr_node=self.head
            prev=None
            while curr_node.next!=None:
                prev=curr_node
                curr_node=curr_node.next
            prev.next=None
            del curr_node
            
    def delete_position(self,position):
        if self.head==None:
            print('Empty Linked List')
        else:
            curr_node=self.head
            prev=None
            count=0
            while curr_node!=None and count<position:
                prev=curr_node
                curr_node=curr_node.next
                count+=1
            if curr_node==self.head:
                self.head=curr_node.next
                del curr_node
            else:
                prev.next=curr_node.next
                del curr_node
                
                
    def count_elements(self):
        count=0
        current=self.head
        while current!=None:
            count+=1
            current=current.next
        print('Number of elements int he linked list are:', count)
        
    def update_value(self,old_val,new_val):
        cur=self.head
        while cur!=None:
            if cur.data==old_val:
                cur.data=new_val
                break
            cur=cur.next
                
    
    def update_position(self,new_element,position):
        if self.head==None and position!=0:
            print('No element to update int the linked list')
        elif self.head==None and position==0:
            new_node=Node(new_element)
            self.head=new_node
            return
        count=0
        current=self.head
        while current.next!=None and current<position:
            count+=1
            current=current.next
        if count==position:
            current.data=new_element
        elif current.next==None:
            print('Not enough elements int he linked list')
            
    
    def sreverse(self):
        prev=None
        cur_node=self.head
        while cur_node!=None:
            nxt=cur_node.next
            cur_node.next=prev
            prev=cur_node
            prev.data=prev.data*(-1)
            cur_node=nxt
        self.head=prev



llist=LinkedList()
llist.head=Node(1)
llist.append(1)
llist.append(2)
llist.append(1.2)
llist.prepend(3)
llist.insert(4,1)
print(llist.traverse())

llist.delete_first()
print(llist.traverse())
llist.delete_last()
print(llist.traverse())
llist.delete_position(1)
print(llist.traverse())
llist.count_elements()
#llist.update_value('John','Bivek')
print(llist.traverse())

llist.sreverse()
print(llist.traverse())