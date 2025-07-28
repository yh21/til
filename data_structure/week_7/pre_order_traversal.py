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

def pre_order(node):
    print(node.data)
    if node.left is not None:
        pre_order(node.left)
    if node.right is not None:
        pre_order(node.right)

pre_order(n1)