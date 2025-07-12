class CQueue:

    def __init__(self, size):
        self.size = size
        self.front = 0
        self.rear = 0
        self.data_list = list()
        for i in range(0, size):
            self.data_list.append(None)

    def enqueue(self, data):
        if (self.rear + 1 - self.front) % self.size == 0:
            print("QUEUE FULL")
        else:
            self.data_list[self.rear] = data
            self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        if (self.front == self.rear):
            print("QUEUE EMPTY")
        else:
            self.data_list[self.front] = None
            self.front = (self.front + 1) % self.size

c = CQueue(5)

c.enqueue('T')
c.enqueue('W')
c.enqueue('O')
c.dequeue()
print(c.data_list)

c.enqueue(1)
c.enqueue(2)
print(c.data_list)

c.enqueue(3)