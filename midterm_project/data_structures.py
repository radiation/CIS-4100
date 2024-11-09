# data_structures.py

from collections import deque

# Queue for managing incoming orders, first in first out
class OrderQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, order):
        self.queue.append(order)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0

# Stack for tracking order fulfillment, last in first out
class FulfillmentStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

# Product definition, with stock management
class Product:
    def __init__(self, product_id, name, author, price, stock):
        self.product_id = product_id
        self.name = name
        self.author = author
        self.price = price
        self.stock = stock

    def __str__(self):
        return (f"Product ID: {self.product_id}, Name: {self.name}, Author: {self.author}, "
                f"Price: ${self.price:.2f}, Stock: {self.stock}")

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            raise ValueError(f"Insufficient stock for Product ID {self.product_id}")

# Node for the Binary Search Tree, it's just product and left/right pointers
class ProductNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None

# Binary Search Tree for managing product catalog, with insert, search, and in-order traversal
class ProductCatalogBST:
    def __init__(self, products):
        self.root = None
        for product in products:
            self.insert(product)

    def insert(self, product):
        new_node = ProductNode(product)
        if not self.root:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if new_node.product.product_id < current.product.product_id:
            if current.left is None:
                current.left = new_node
            else:
                self._insert(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert(current.right, new_node)

    def search(self, product_id):
        return self._search(self.root, product_id)

    def _search(self, current, product_id):
        if current is None or current.product.product_id == product_id:
            return current
        if product_id < current.product.product_id:
            return self._search(current.left, product_id)
        return self._search(current.right, product_id)

    def update_stock(self, product_id, quantity):
        node = self.search(product_id)
        if node:
            try:
                node.product.reduce_stock(quantity)
                print(f"Updated stock for {node.product.name}: New stock is {node.product.stock}")
                return node.product
            except ValueError as e:
                print(e)
                return None
        else:
            print(f"Product ID {product_id} not found.")
            return None

    def in_order_traversal(self):
        products = []
        self._in_order(self.root, products)
        return products

    def _in_order(self, current, products):
        if current:
            self._in_order(current.left, products)
            products.append(current.product)
            self._in_order(current.right, products)
