class AVL:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def __insertion__(self, node, data):
        if node is None:
            return AVL(data)
        elif node.data > data:
            node.left = self.__insertion__(node.left, data)
        elif node.data < data:
            node.right = self.__insertion__(node.right, data)

        node.height = self.__height__(node)
        balance = self.__height__(node.left) - self.__height__(node.right)

        if balance > 1:
            if node.left.data > data:
                return self.__right_rotation__(node)
            else:
                node.left = self.__left_rotation__(node.left)
                return self.__right_rotation__(node)
        if balance < -1:
            if node.right.data < data:
                return self.__left_rotation__(node)
            else:
                node.right = self.__right_rotation__(node.right)
                return self.__left_rotation__(node)

        return node

    def __delete__(self, node, data):
        if node is None:
            return node
        elif node.data > data:
            node.left = self.__delete__(node.left, data)
        elif node.data < data:
            node.right = self.__delete__(node.right, data)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            else:
                temp = self.__minimum_value__(node.right)
                node.data = temp.data
                node.right = self.__delete__(node.right, temp.data)
                node.height = self.__height__(node)

            balance = self.__height__(node.left) - self.__height__(node.right)
            var = self.__height__(node.left.left) - self.__height__(node.left.right)
            if balance > 1:
                if var >= 0:
                    return self.__right_rotation__(node)
                else:
                    node.left = self.__left_rotation__(node.left)
                    return self.__right_rotation__(node)
            elif balance < -1:
                if var <= 0:
                    return self.__left_rotation__(node)
                else:
                    node.right = self.__right_rotation__(node.right)
                    return self.__left_rotation__(node)

            return node

    def __height__(self, node):
        if node is None:
            return 0
        else:
            left = self.__height__(node.left)
            right = self.__height__(node.right)
            return 1 + max(left, right)

    def __right_rotation__(self, node):
        lefty = node.left
        temp = lefty.right
        lefty.right = node
        node.left = temp
        node.height = self.__height__(node)
        lefty.height = self.__height__(lefty)
        return lefty

    def __left_rotation__(self, node):
        righty = node.right
        temp = righty.left
        righty.left = node
        node.right = temp
        node.height = self.__height__(node)
        righty.height = self.__height__(righty)
        return righty

    def __minimum_value__(self, node):
        if node.left is None or node is None:
            return node
        else:
            return self.__minimum_value__(node.left)

    def __noorder_traversal__(self, node):
        current_node = node
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


if __name__ == '__main__':
    print('AVL Testing For Left Rotation: ')
    avl1 = AVLTree()
    root1 = None
    list1 = [40, 50, 60, 45, 55, 70]
    for i in list1:
        root1 = avl1.__insertion__(root1, i)
    result1 = avl1.__noorder_traversal__(root1)
    print(f'Left Rotated: {result1}')

    print('AVL Testing For Right Rotation: ')
    avl2 = AVLTree()
    root2 = None
    list2 = [40, 30, 20, 35, 10, 25]
    for i in list2:
        root2 = avl2.__insertion__(root2, i)
    result2 = avl2.__noorder_traversal__(root2)
    print(f'Right Rotated: {result2}')
    print('')
    print('Delete A Node:')
    print('Create A Tree:')
    avl3 = AVLTree()
    root3 = None
    list3 = [60, 50, 70, 40, 55, 65, 75, 35, 45]
    for i in list3:
        root3 = avl3.__insertion__(root3, i)
    result3 = avl2.__noorder_traversal__(root3)
    print(f'Traversed: {result3}')
    print('Deletion:')
    avl3.__delete__(root3, 50)
    result3 = avl2.__noorder_traversal__(root3)
    print(f'Traversed: {result3}')
