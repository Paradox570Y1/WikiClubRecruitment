# Product data: (Product ID, Price, Stock Quantity)
products: list[tuple[str, float | str, int]] = [ # notice the type hinted variables
    ("p001", 150.00, 5),
    ("p002", 200.00, 0),
    ("p003", 50.50, 10),
    ("p004", "99.99", 3),   # input is a string, not a float
    ("p005", 300.00, 0),
    ("p006", 75.00, -1)    # Converting negative stocks to 0
]


def process_stock(product_list):
    total_value = 0
    out_of_stock_items = []

    for product in product_list:
        stock_id, stock_price, stock_qty = product
        # Calculate the value of each product in stock
        
        try:
            stock_price = float(stock_price)
        except Exception as e:
            stock_price = 0
        
        try:
            stock_qty = int(stock_qty)
        except Exception as e:
            stock_qty = 0
        
        if stock_qty < 0:
            stock_qty = 0
        
        stock_value = stock_price * stock_qty

        total_value += stock_value

        # Check for out of stock items
        if stock_value == 0:
            out_of_stock_items.append(stock_id)

    return total_value, out_of_stock_items


stock_value, out_of_stock = process_stock(products)

print(f"Total value of all stock: {stock_value}")
print(f"Out of stock products: {out_of_stock}")
