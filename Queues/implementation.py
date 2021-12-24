class queue:

    def __init__(self):
        l = []
        self.l = l

    def enqueue(self, element):
        self.l.append(element)
        return self.l

    def dequeue(self):
        if len(self.l) > 0 :
            self.l.pop(0)
        else:
            print('queue is empty')

    def front(self):
        if len(self.l) > 0:
            return self.l[0]
        else:
            print('queue is empty')

    def rear(self):
        if len(self.l) > 0:
            return self.l[len(self.l)-1]

