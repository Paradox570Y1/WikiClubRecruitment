

# Stock Management Module
#
# This file has the main stuff for our stock project.
# We have a list of products, and a function to check how much all products are worth
# and which ones are out of stock.


from typing import List, Tuple, Union


# Each product is a tuple: (product id, price, quantity)
Product = Tuple[str, Union[float, str], int]


# Here are some products to test with
products: List[Product] = [
    ("p001", 150.00, 5),      # normal product
    ("p002", 200.00, 0),      # out of stock
    ("p003", 50.50, 10),      # normal product
    ("p004", "99.99", 3),    # price is a string
    ("p005", 300.00, 0),      # out of stock
    ("p006", 75.00, -1)       # negative stock (should be 0)
]


def process_stock(product_list: List[Product]) -> Tuple[float, List[str]]:
    # This function checks all products and tells us:
    # - How much all products are worth together
    # - Which products are out of stock
    total_value = 0
    out_of_stock_items = []

    for product in product_list:
        stock_id, stock_price, stock_qty = product

        # Try to make sure price is a number
        try:
            stock_price = float(stock_price)
        except Exception:
            stock_price = 0

        # Try to make sure quantity is a number and not negative
        try:
            stock_qty = int(stock_qty)
        except Exception:
            stock_qty = 0
            
        if stock_qty < 0:
            stock_qty = 0

        # Calculate how much this product is worth
        stock_value = stock_price * stock_qty
        total_value += stock_value

        # If product is worth 0, it's out of stock
        if stock_value == 0:
            out_of_stock_items.append(stock_id)

    return total_value, out_of_stock_items