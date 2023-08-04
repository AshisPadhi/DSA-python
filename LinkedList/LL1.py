class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self, value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        self.length=1

    def printList(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length += 1

    def prepend(self, val):
        tmp=Node(val)
        if not self.head:
            self.head=tmp
            self.head.next=None
        else:
            tmp.next=self.head
            self.head=tmp

    def pop (self):
        tmp=self.head
        prev=self.tail
        val=None
        if tmp==prev:
            val=tmp.value
            self.head.next=None
            self.tail.next=None
            self.length=0
        elif tmp.value==None:
            val=None
        else:
            while tmp.next:
                prev=tmp
                tmp=tmp.next
            val=tmp.value
            self.tail=prev
            self.tail.next=None
            self.length-=1
        return val


myLinkedList=LinkedList(4)
myLinkedList.append(5)
myLinkedList.append(8)
myLinkedList.append(1)
#print(myLinkedList.head.value)
myLinkedList.printList()
#print("popping now")
#print(myLinkedList.pop())
#print(myLinkedList.pop())
myLinkedList.prepend(6)
print("printing after prepending")
print(myLinkedList.printList())
