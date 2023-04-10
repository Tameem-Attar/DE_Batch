import unittest
from product import Product
from shoppingcart import ShoppingCart


class TestShoppingCart(unittest.TestCase):


    def setUp(self):
        self.cart = ShoppingCart()


    def test_add_item(self):

        # Test adding a single item to the cart
        item = Product('Shirt', 20)
        self.cart.add_item(item)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].name, 'Shirt')
        self.assertEqual(self.cart.items[0].price, 20)


        # Test adding multiple items to the cart
        item2 = Product('Pants', 30)
        self.cart.add_item(item2)
        self.assertEqual(len(self.cart.items), 2)
        self.assertEqual(self.cart.items[1].name, 'Pants')
        self.assertEqual(self.cart.items[1].price, 30)


    def test_remove_item(self):

        # Test removing an item that exists in the cart
        item = Product('Shirt', 20)
        self.cart.add_item(item)
        self.cart.remove_item(item)
        self.assertEqual(len(self.cart.items), 0)
        

        # Test removing an item that does not exist in the cart
        item2 = Product('Pants', 30)
        self.cart.remove_item(item2)
        self.assertEqual(len(self.cart.items), 0)


    def test_get_total_price(self):

        # Test getting the total price of an empty cart
        self.assertEqual(self.cart.get_total_price(), 0)


        # Test getting the total price of a cart with items
        item = Product('Shirt', 20)
        self.cart.add_item(item)
        item2 = Product('Pants', 30)
        self.cart.add_item(item2)
        self.assertEqual(self.cart.get_total_price(), 50)


if __name__ == '__main__':
    unittest.main()

    


