
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class binaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        temp = self.root
        while temp is not None:
            print(temp.data)
            if (temp.data > val):
                temp = temp.left
            if temp.data < val:
                temp = temp.right
        if temp.data > val:
            temp.left = Node(val)
        else:
            temp.right = Node(val)


tree = binaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(80)
