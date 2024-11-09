from data_structures import Product

import csv
import random
import time

# Load products from a CSV file, duh
def load_products_from_csv(file_path):
    products = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product_id = int(row['product_id'])
            title = row['title']
            author = row['author']
            price = float(row['price'])
            stock = int(row['stock'])
            products.append(Product(product_id, title, author, price, stock))
    return products

# Load orders from a CSV file, duh
def load_orders_from_csv(file_path):
    orders = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items = []
            for item in row['items'].split(';'):
                product_id, quantity = map(int, item.split(':'))
                items.append({'product_id': product_id, 'quantity': quantity})
            orders.append({
                'customer': row['customer_name'],
                'items': items
            })
    return orders

# Add orders to the queue, kinda obvious
def add_orders_to_queue(order_queue, orders):
    for order in orders:
        order_queue.enqueue(order)

# Process orders, fulfill them, and update the catalog, less obvious
def process_orders(order_queue, product_catalog, fulfillment_stack):
    while not order_queue.is_empty():
        order = order_queue.dequeue()
        print(f"\nProcessing order for {order['customer']}")

        items_fulfilled = []
        for item in order['items']:
            node = product_catalog.search(item['product_id'])
            if node and node.product.stock >= item['quantity']:
                product_catalog.update_stock(item['product_id'], item['quantity'])
                items_fulfilled.append(item)
                print(f"Fulfilled {item['quantity']} of {node.product.name}")
            else:
                print(f"Insufficient stock for product ID {item['product_id']}")

        for item in items_fulfilled:
            fulfillment_stack.push(item)

        time.sleep(random.uniform(0.5, 2.0))

# Process fulfilled orders and ship them
def ship_orders(fulfillment_stack):
    print("\nShipping items:")
    while not fulfillment_stack.is_empty():
        item = fulfillment_stack.pop()
        print(f"Shipping {item['quantity']} of product ID {item['product_id']}")
