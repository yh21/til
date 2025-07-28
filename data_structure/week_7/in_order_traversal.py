class BinaryClassNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

n1 = BinaryClassNode(93)
n2 = BinaryClassNode(15)
n3 = BinaryClassNode(19)
n4 = BinaryClassNode(36)
n5 = BinaryClassNode(44)
n6 = BinaryClassNode(72)
n7 = BinaryClassNode(83)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.left = n6
n5.right = n7

def in_order(node):
    if node.left is not None:
        in_order(node.left)
    print(node.data)
    if node.right is not None:
        in_order(node.right)

in_order(n1)