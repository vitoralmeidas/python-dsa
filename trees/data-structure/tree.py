# tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        self.insert_node(self.root, val)

    def insert_node(self, node, val):
        if val <= node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.insert_node(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self.insert_node(node.right, val)

    def search(self, val):
        return self.search_node(self.root, val)

    def search_node(self, node, val):
        if node is None:
            return False
        if node.val == val:
            return True
        if val <= node.val:
            return self.search_node(node.left, val)
        else:
            return self.search_node(node.right, val)

    def delete(self, val):
        self.root = self.delete_node(self.root, val)

    def delete_node(self, node, val):
        if node is None:
            return node
        if val < node.val:
            node.left = self.delete_node(node.left, val)
        elif val > node.val:
            node.right = self.delete_node(node.right, val)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.get_min(node.right)
            node.val = temp.val
            node.right = self.delete_node(node.right, temp.val)
        return node

    def get_min(self, node):
        if node.left is None:
            return node
        return self.get_min(node.left)

    def get_max(self, node):
        if node.right is None:
            return node
        return self.get_max(node.right)

    def traverse_in_order(self):
        self.traverse_in_order_node(self.root)

    def traverse_in_order_node(self, node):
        if node is None:
            return
        self.traverse_in_order_node(node.left)
        print(node.val)
        self.traverse_in_order_node(node.right)

    def traverse_pre_order(self):
        self.traverse_pre_order_node(self.root)

    def traverse_pre_order_node(self, node):
        if node is None:
            return
        print(node.val)
        self.traverse_pre_order_node(node.left)
        self.traverse_pre_order_node(node.right)
