class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    # add to end of list
    def append(self,value):
        new_node = Node(value)
        if self.head is None: # list is emptytt
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        self.length += 1
    def pop(self):#delete from tail
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre =temp
            while temp.next:
                pre = temp
                temp = temp.next
        self.tail = pre
        pre.next = None
        self.length-=1
        if self.length == 0:
            self.head = None
            self.tail = None

    def prepend(self,value):#add to first
        new_node = Node(value)
        if self.head is  None:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length +=1
    def popfirst(self):#delte from first
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None

    def get(self, index):#get node by index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def set_value(self,index,value):#set value at index
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self,index,value):# insert at index
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
    def remove(self, index):#remove at index
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -=1
    def reverse(self):#revers the list
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        befor = None
        while temp:
            after = temp.next
            temp.next = befor
            befor = temp
            temp = after
            


linkedlist = LinkedList(5)
linkedlist.append(4)
linkedlist.append(48)
linkedlist.prepend(89)
linkedlist.insert(4,122)
linkedlist.reverse()
linkedlist.print_list()