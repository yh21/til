class Node:

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

def node_insert(value, position):
    new_node = Node(value, position, position.next)
    new_node.prev.next = new_node
    new_node.next.prev = new_node
    return new_node

def node_delete(input_node):
    input_node.prev.next = input_node.next
    input_node.next.prev = input_node.prev

def visit_all(input_node):
    now_node = input_node
    while (True):
        print(now_node.data)
        now_node = now_node.next
        if (now_node.data) == None:
            break

head = Node(None, None, None)
tail = Node(None, None, None)

head.next = tail
tail.prev = head

N1 = node_insert('yh', head)
N2 = node_insert('km', N1)
N3 = node_insert('jh', head)
node_delete(N2)

visit_all(head)