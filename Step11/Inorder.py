class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


    def insertleft(self,data):
        if self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            self.data = data

    def insertright(self,data):
        if self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insertright(data)
        else:
            self.data = data
def printInorder(root):
        if root:
 
        # First recur on left child
            printInorder(root.left)
 
        # then print the data of node
            print(root.data),
 
        # now recur on right child
            printInorder(root.right)

root = Node(28)
root.insertleft(15)
root.insertright(65)
root.insertright(60)
printInorder(root)


