import unittest
from product import Product
from shoppingcart import ShoppingCart
from test_shoppingcart import TestShoppingCart

def main():
    cart = ShoppingCart()
    apple = Product("apple", 0.5)
    banana = Product("banana", 0.3)
    cart.add_item(apple)
    cart.add_item(banana)
    print(f"Total price: ${cart.get_total_price():.2f}")
    cart.remove_item(apple)
    print(f"Total price: ${cart.get_total_price():.2f}")

if __name__ == "__main__":
    main()
    suite=unittest.TestSuite()
    suite.addTest(TestShoppingCart("test_add_item"))
    suite.addTest(TestShoppingCart("test_remove_item"))
    suite.addTest(TestShoppingCart("test_get_total_price"))
    suite.addTest(TestShoppingCart("test_check_type"))
    runner=unittest.TextTestRunner()
    runner.run(suite)
