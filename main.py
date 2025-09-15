# Main Runner Script
#
# This is the main file for our stock project.
# It shows how much all the products are worth together,
# and which products are not available (out of stock).
#
# To run this, just use:
#   python main.py

from stock.stock import products, process_stock

def main():
    # This function gets the total value and out of stock products
    stock_value, out_of_stock = process_stock(products)

    # Print the results
    print(f"Total value of all stock: {stock_value}")
    print(f"Out of stock products: {out_of_stock}")

if __name__ == "__main__":
    main()