from product import Product
from shoppingcart import ShoppingCart
import unittest

def main():
    cart = ShoppingCart()
    apple = Product("apple", 0.5)
    banana = Product("banana", 0.3)
    cart.add_item(apple)
    cart.add_item(banana)
    print(f"Total price: ${cart.get_total_price():.2f}")
    cart.remove_item(apple)
    print(f"Total price: ${cart.get_total_price():.2f}")
class unit_testing_the_cart(unittest.TestCase):
    def test_item_removed_or_not(self):
        apple = Product("apple",50.0)
        banana = Product("banana",30.0)
        cart = ShoppingCart()
        cart.add_item(apple)
        self.assertEqual(cart.remove_item(apple),"Item removed successfully")
        self.assertEqual(cart.remove_item(banana),"Item not present in the cart")
    def test_item_added_or_not(self):
        apple = ("apple",50.0)
        banana = ("banana",30.0)
        cart = ShoppingCart()
        self.assertEqual(cart.add_item(apple),"Item added successfully")
    def test_the_item_raise_the_error(self):
        with self.assertRaises(TypeError):
            apple=Product(True,50.0)
        with self.assertRaises(TypeError):
            apple=Product("apple","50.0")
        with self.assertRaises(ValueError):
            apple=Product("apple",-50.0)

if __name__ == "__main__":
    main()
    unittest.main()