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

myLinkedList=LinkedList(4)
myLinkedList.append(5)
myLinkedList.append(8)
#print(myLinkedList.head.value)
myLinkedList.printList()
