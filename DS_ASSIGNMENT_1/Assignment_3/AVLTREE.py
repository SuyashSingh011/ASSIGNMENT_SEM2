

class Node:
    def __init__(self, value):
        self.value = value
        self.height = 0
        self.balanceFactor = 0
        self.left = None
        self.right = None
        self.size = 1  # For tracking the size of the subtree for order statistics

class AvlTree:
    def __init__(self):
        self.__nodesCount = 0
        self.__root = None
    
    def find(self, value):
        return self.__contains(self.__root, value)
    
    def __contains(self, node, target):
        if node is None:
            return False
        if node.value == target:
            return True
        if target > node.value:
            return self.__contains(node.right, target)
        else:
            return self.__contains(node.left, target)

    def insert(self, value):
        if value is None:
            return False
        if self.find(value):
            return False
        else:
            self.__root = self.__insert(self.__root, value)
            self.__nodesCount += 1
            return True

    def __insert(self, node, target):
        if node is None:
            return Node(target)
        if target > node.value:
            node.right = self.__insert(node.right, target)
        else:
            node.left = self.__insert(node.left, target)
        self.__update(node)
        return self.__balance(node)

    def __update(self, node):
        leftHeight, rightHeight = -1, -1
        leftSize, rightSize = 0, 0

        if node.left is not None:
            leftHeight = node.left.height
            leftSize = node.left.size
        
        if node.right is not None:
            rightHeight = node.right.height
            rightSize = node.right.size
        
        node.height = 1 + max(leftHeight, rightHeight)
        node.size = 1 + leftSize + rightSize
        node.balanceFactor = rightHeight - leftHeight

    def __balance(self, node):
        if node.balanceFactor == +2:
            if node.right.balanceFactor >= 0:
                return self.__rightRightCase(node)
            else:
                return self.__rightLeftCase(node)
        elif node.balanceFactor == -2:
            if node.left.balanceFactor <= 0:
                return self.__leftLeftCase(node)
            else:
                return self.__leftRightCase(node)
        return node
    
    def __leftLeftCase(self, node):
        return self.__rotateRight(node)
    
    def __leftRightCase(self, node):
        node.left = self.__rotateLeft(node.left)
        return self.__leftLeftCase(node)
    
    def __rightRightCase(self, node):
        return self.__rotateLeft(node)
    
    def __rightLeftCase(self, node):
        node.right = self.__rotateRight(node.right)
        return self.__rightRightCase(node)
    
    def __rotateRight(self, node):
        B = node.left
        node.left = B.right
        B.right = node
        self.__update(node)
        self.__update(B)
        return B

    def __rotateLeft(self, node):
        B = node.right
        node.right = B.left
        B.left = node
        self.__update(node)
        self.__update(B)
        return B

    def remove(self, value):
        if value is None:
            return False
        if not self.find(value):
            return False
        else:
            self.__root = self.__remove(self.__root, value)
            self.__nodesCount -= 1
            return True

    def __remove(self, node, target):
        if node.value == target:
            if node.left is None and node.right is None:
                del node
                return None
            elif node.left is None:
                temp = node.right
                del node
                return temp
            elif node.right is None:
                temp = node.left
                del node
                return temp
            else:
                successor = node.left
                while successor.right is not None:
                    successor = successor.right
                node.value = successor.value
                node.left = self.__remove(node.left, successor.value)
                self.__update(node)
                return self.__balance(node)
        elif target > node.value:
            node.right = self.__remove(node.right, target)
        else:
            node.left = self.__remove(node.left, target)
        self.__update(node)
        return self.__balance(node)
    
    def order_of_key(self, key):
        return self.__order_of_key(self.__root, key)

    def __order_of_key(self, node, key):
        if node is None:
            return 0
        if key <= node.value:
            return self.__order_of_key(node.left, key)
        else:
            leftSize = 0 if node.left is None else node.left.size
            return 1 + leftSize + self.__order_of_key(node.right, key)

    def get_by_order(self, k):
        if k < 0 or k >= self.__nodesCount:
            return None
        return self.__get_by_order(self.__root, k + 1)

    def __get_by_order(self, node, k):
        leftSize = 0 if node.left is None else node.left.size
        if k <= leftSize:
            return self.__get_by_order(node.left, k)
        elif k == leftSize + 1:
            return node.value
        else:
            return self.__get_by_order(node.right, k - leftSize - 1)

tree = AvlTree()
tree.insert(10)
tree.insert(20)
tree.insert(5)
tree.insert(15)

print(tree.find(10))  
print(tree.find(25))  
print(tree.order_of_key(15)) 
print(tree.get_by_order(2))  

tree.remove(10)
print(tree.find(10))  
