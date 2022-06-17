class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __building_bst__(self, depth):
        current_node = self.root

        def __building__(node, level, num):
            if level >= 2:
                if node is None:
                    node = Tree(num)
                level -= 1
                node.left = __building__(node.left, level, num - level * level)
                node.right = __building__(node.right, level, num + level * level)
            return node

        self.root = __building__(current_node, depth, 50)

    def __noorder_traversal__(self):
        current_node = self.root
        q = [current_node]

        def __traversal__(q, traversal):
            if q:
                info = q.pop(0)
                traversal += str(info.data) + '->'
                if info.left:
                    q.append(info.left)
                if info.right:
                    q.append(info.right)
                traversal = __traversal__(q, traversal)
            return traversal

        result = __traversal__(q, '')
        return result

    def __insert_a_node__(self, data):
        current_node = self.root

        def __inserting__(node, key):
            if node:
                if node.left and node.right and node.left.data < key < node.right.data:
                    temp = node.data
                    node.data = key
                    __inserting__(node.left, temp)

                elif node.left and node.left.data > key:
                    __inserting__(node.left, key)

                elif node.right and node.right.data < key:
                    __inserting__(node.right, key)

                elif node.left is None and node.right is None:
                    if node.data > key:
                        node.left = Tree(key)

                    else:
                        node.right = Tree(key)

        __inserting__(current_node, data)
        print(f'This Node Has Changed It\'s Position: {self.root.right.right.left.right.data}')

    def __deleting_a_node__(self, data):
        current_node = self.root

        def __deletion__(node, key):
            if node:
                if node.data == key and node == self.root:
                    if node.left is None and node.right is None:
                        self.root = None
                    elif node.left.right is None and node.left.left is None and node.right.left is None and node.right.right is None:
                        temp = node.left
                        self.root = node.right
                        self.root.left = temp
                    elif node.left is None and node.right is not None:
                        temp = node.right
                        self.root = __inorder__(node.right)
                        self.root.right = temp
                    elif node.right is None and node.left is not None:
                        temp = node.left
                        self.root = __inorder__(node.left)
                        self.root.left = temp
                    elif node.left is not None and node.right is not None:
                        temp1 = node.left
                        temp2 = node.right
                        self.root = __inorder__(node.right)
                        self.root.left = temp1
                        self.root.right = temp2

                elif node.left.data == key:
                    if node.left.left is None and node.left.right is None:
                        node.left = None
                    elif node.left.left.left is None and node.left.left.right is None:
                        temp = node.left.left
                        node.left = node.left.right
                        node.left.right = None
                        node.left.left = temp
                    elif node.left.left is None and node.left.right is not None:
                        temp = node.left.right
                        node.left = __inorder__(node.left.right)
                        node.left.right = temp
                    elif node.left.right is None and node.left.left is not None:
                        temp = node.left.left
                        node.left = __inorder__(node.left.left)
                        node.left.left = temp
                    elif node.left.left is not None and node.left.right is not None:
                        temp1, temp2 = node.left.left, node.left.right
                        node.left = __inorder__(node.left.right)
                        node.left.left = temp1
                        node.left.right = temp2

                elif node.right.data == key:
                    if node.right.left is None and node.right.right is None:
                        node.right = None
                    elif node.right.right.right is None and node.right.right.left is None:
                        temp = node.right.left
                        node.right = node.right.right
                        node.right.right = None
                        node.right.left = temp
                    elif node.right.left is None and node.right.right is not None:
                        temp = node.right.right
                        node.right = __inorder__(node.right.right)
                        node.right.right = temp
                    elif node.right.right is None and node.right.left is not None:
                        temp = node.right.left
                        node.right = __inorder__(node.right.left)
                        node.right.left = temp
                    elif node.right.right is not None and node.right.left is not None:
                        temp1, temp2 = node.right.right, node.right.left
                        node.right = __inorder__(node.right.right)
                        node.right.right = temp1
                        node.right.left = temp2

                else:
                    if node.left and node.data > key:
                        __deletion__(node.left, key)
                    if node.right and node.data < key:
                        __deletion__(node.right, key)

        def __inorder__(node):
            if node.left.left:
                node = __inorder__(node.left)
                return node
            else:
                temp = node.left
                node.left = None
                return temp

        __deletion__(current_node, data)


if __name__ == '__main__':
    bst = BinarySearchTree()
    x = int(input('Enter The Depth Of The Tree: '))  # Level is a non-negative integer number
    x += 2
    bst.__building_bst__(x)
    print(f'Level Wise Traversal: {bst.__noorder_traversal__()}')
    print('Insert a Node')
    bst.__insert_a_node__(76)
    print(f'Level Wise Traversal: {bst.__noorder_traversal__()}')
    print('Delete A Node')
    bst.__deleting_a_node__(76)
    print(f'Level Wise Traversal: {bst.__noorder_traversal__()}')
