# @XuRUn: 04/2021

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.__str__()

class BinaryTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break

def preOrder(root):
    if root != None:
        print(root.value, end = ' ')
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root != None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.value, end = ' ')

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.value, end = ' ')
        inOrder(root.right)


tree = BinaryTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)