class node:
    def __init__(self,data = None) :
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self) :
        self.head = node()

    def append(self,data) :
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self) :
        total = 0
        cur = self.head
        while cur.next != None:
            total +=1
            cur = cur.next
        return total

    def display(self) :
        l = []
        cur = self.head
        while cur.next != None :
            cur = cur.next
            l.append(cur.data)
        return l

    def get(self,index) :
        if index > self.length()-1:
            print('ERROR')
            return
        cur = self.head
        i = 0
        while cur.next != None:
            cur = cur.next
            if i == index:
                return cur.data
            i +=1

    def erase(self,index) :
        if index > self.length() - 1:
            print('Error')
            return
        cur = self.head
        i = 0
        while cur.next != None:
            last = cur
            cur = cur.next
            if index == i:
                last.next = cur.next
                return
            i +=1


