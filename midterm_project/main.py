# main.py

from data_structures import OrderQueue, FulfillmentStack, ProductCatalogBST
from order_manager import load_orders_from_csv, add_orders_to_queue, process_orders, ship_orders, load_products_from_csv

if __name__ == "__main__":
    # Initialize structures
    order_queue = OrderQueue()
    fulfillment_stack = FulfillmentStack()

    # Load products from CSV and create the BST
    products = load_products_from_csv('products.csv')
    product_catalog = ProductCatalogBST(products)

    # Print initial product catalog
    print("Initial Product Catalog:")
    for product in product_catalog.in_order_traversal():
        print(product)

    # Load orders from CSV and add them to the queue
    orders = load_orders_from_csv('orders.csv')
    add_orders_to_queue(order_queue, orders)

    # Process and fulfill orders, this reads all the CSVs and processes the orders
    process_orders(order_queue, product_catalog, fulfillment_stack)

    # Ship orders
    ship_orders(fulfillment_stack)

    # Print the final product catalog from the tree
    print("\nFinal Product Catalog:")
    for product in product_catalog.in_order_traversal():
        print(product)
