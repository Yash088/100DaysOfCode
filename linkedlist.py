class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if(self.head == None):
            self.head = Node(val)
            return "Inserted"
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(val)

    def push(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def insertPos(self, pos, val):
        temp = self.head
        count = 1
        while count < pos-1:
            temp = temp.next
            count += 1
        new_node = Node(val)
        new_node.next = temp.next
        temp.next = new_node

    def pop(self):
        if self.head == None:
            return "Empty"
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        return "Poped"

    def deletePos(self, pos):
        if self.head == None:
            return "Empty"
        temp = self.head
        count = 1
        while count < pos-1:
            temp = temp.next
            count += 1
        res = temp.next.data
        temp.next = temp.next.next
        return str(res) + "Is deleted at pos" + str(pos)

    def printList(self):
        temp = self.head
        res = ''
        while temp.next:
            res += str(temp.data) + "->"
            temp = temp.next
        print(res)


ll = linkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.printList()
# ll.pop()
ll.deletePos(2)
ll.printList()

# ll.append(4)
# ll.append(5)
