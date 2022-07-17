class Node:
    def __init__(self, data):
        # Heads of terms
        self.left = None  # Default value
        self.right = None  # Default value
        self.data = data  # Start node

    # Add node
    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:  # if start node exist
            if data < self.data:  # if node's value which would you like add is smaller than 'parent' node
                if self.left is None:  # if left side not exist
                    self.left = Node(data)  # add root and set value
                else:  # if left side exist
                    self.left.insert(data)  # return to start of insert (go up one position)
            elif data > self.data:  # if node's value which would you like add is greater than 'parent' node
                if self.right is None:  # if right side not exist
                    self.right = Node(data)  # add root and set value
                else:  # if right side exist
                    self.right.insert(data)  # return to start of insert (go up one position)

        else:  # if start node not exist
            self.data = data

    # Search node
    def find(self, y):
        if y < self.data:
            if self.left is None:
                return str(y) + ' Not found'
            return self.left.find(y)
        elif y > self.data:
            if self.right is None:
                return str(y) + ' Not found'
            return self.right.find(y)
        else:
            return str(self.data) + ' is found'

    # Print the tree
    def PrintTree(self):  # Recursive func
        if self.left:
            self.left.PrintTree()

        if self.right:
            self.right.PrintTree()

        print(self.data)

    # Inorder traversal
    # Left -> Root -> Right
    # x is variable like root from main, which store actual value
    def Inorder(self, x):
        res = []
        if x:
            res = self.Inorder(x.left)
            res.append(x.data)
            res += self.Inorder(x.right)
        return res

    # Preorder traversal
    # Root -> Left -> Right
    def Preorder(self, x):
        res = []
        if x:
            res.append(x.data)
            res += self.Preorder(x.left)
            res += self.Preorder(x.right)
        return res

    # Postorder traversal
    # Left -> Right -> Root
    def Postorder(self, x):
        res = []
        if x:
            res = self.Postorder(x.left)
            res += self.Postorder(x.right)
            res.append(x.data)
        return res


if __name__ == '__main__':

    while True:
        add_node = input('Enter nodes to insert, space is separator: ')
        lst = add_node.split()
        try:
            start_node = int(lst[0])

            root = Node(start_node)
            for i in range(1, len(lst)):
                root.insert(int(lst[i]))

            print(root.Postorder(root))
            break
        except (ValueError, IndexError) as e:
            print(e)

    print(root.find(31))

    # Test input: 10 19 14 31 42 35 27
