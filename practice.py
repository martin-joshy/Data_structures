class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, val):
        if self.data == val:
            return True
        if self.left.data > val:
            self.left.search(val)
        elif self.right.data < val:
            self.right.search(val)

    def add_child(self, data):
        pass

    def in_order_traversal(self):
        pass

    def find_max(self):
        pass

    def delete(self, val):
        pass