class Stack:
    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        if(self.arr):
            return self.arr.pop()
        return -1

    def isEmpty(self):
        if(not self.arr):
            return True
        return False

    def peek(self):
        if(self.isEmpty()):
            return "Empty Stack"
        return self.arr[-1]


stk = Stack()
while True:
    command = input().split()
    if(int(command[0]) == 1):
        stk.push(int(command[1]))
    elif(len(command) == 1):
        if(int(command[0]) == 2):
            print(stk.pop())
        if(int(command[0]) == 3):
            print(stk.isEmpty())
        if(int(command[0]) == 4):
            print(stk.peek())
    else:
        print("Unknown command : 1 -> Push value, 2 -> Pop")
