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

myLinkedList=LinkedList(4)
#print(myLinkedList.head.value)
myLinkedList.printList()