
# Test Cases for Stock Module
#
# This file checks if our stock code works right.
# It tests if the total value is correct and finds which products are out of stock.
#
# To run these tests, just do:
#   python test_stock.py

import sys
import os
# Add the parent directory to sys.path so we can import the stock module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from stock.stock import process_stock, products

def test_total_stock_value():
    # This test checks if the total value of all products is right.
    # We add up each product's value and see if it matches.
    total_value, _ = process_stock(products)
    expected_total = 750 + 0 + 505 + 299.97 + 0 + 0
    assert abs(total_value - expected_total) < 0.01  # allow small float rounding

def test_out_of_stock_products():
    # This test checks if we find the right products that are out of stock.
    _, out_of_stock = process_stock(products)
    expected_out_of_stock = ["p002", "p005", "p006"]
    assert sorted(out_of_stock) == sorted(expected_out_of_stock)

def test_negative_stock_handling():
    # This test checks if negative stock is treated as zero.
    test_products = [("p100", 50.0, -5)]
    total_value, out_of_stock = process_stock(test_products)
    assert total_value == 0
    assert out_of_stock == ["p100"]

def test_string_price_conversion():
    # This test checks if prices given as strings work fine.
    test_products = [("p200", "123.45", 2)]
    total_value, _ = process_stock(test_products)
    assert abs(total_value - (123.45 * 2)) < 0.01

def test_invalid_price_and_quantity():
    # This test checks if wrong price or quantity is handled as zero.
    test_products = [("p300", "abc", "xyz")]
    total_value, out_of_stock = process_stock(test_products)
    assert total_value == 0
    assert out_of_stock == ["p300"]

if __name__ == "__main__":
    # Run all tests
    test_total_stock_value()
    test_out_of_stock_products()
    test_negative_stock_handling()
    test_string_price_conversion()
    test_invalid_price_and_quantity()
    print("All tests passed!")
