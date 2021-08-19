class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def size(node):
    if node is None:
        return 0
    else:
        return (size(node.left)+size(node.right)+1)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("Size of the given tree is ",size(root))
