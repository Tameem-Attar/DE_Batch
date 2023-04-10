import unittest 
from product import Product
from shoppingcart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def test_add_item(self):
        cart=ShoppingCart()
        #self.assertEqual(cart.get_total_price(),0.0)
        watermelon=Product("watermelon",1.0)
        cart.add_item(watermelon)
        #self.assertEqual(cart.get_total_price(),1.0)
        self.assertTrue(watermelon in cart.items)
    def test_remove_item(self):
        cart=ShoppingCart()
        #self.assertEqual(cart.get_total_price(),0.0)
        watermelon=Product("watermelon",1.0)
        cart.add_item(watermelon)
        #self.assertEqual(cart.get_total_price(),1.0)
        cart.remove_item(watermelon)
        #self.assetEqual(cart.get_total_price(),0.0)
        self.assertTrue(watermelon not in cart.items)
    def test_get_total_price(self):
        cart=ShoppingCart()
        self.assertEqual(cart.get_total_price(),0.0)
        watermelon=Product("watermelon",1.0)
        cart.add_item(watermelon)
        self.assertEqual(cart.get_total_price(),1.0)
        apple=Product("apple",0.8)
        cart.add_item(apple)
        self.assertEqual(cart.get_total_price(),1.8)
    def test_check_type(self):
        with self.assertRaises(TypeError):
            watermelon=Product("watermelon",1)
        with self.assertRaises(TypeError):
            watermelon=Product("watermelon","1.0")
        with self.assertRaises(ValueError):
            watermelon=Product("watermelon",-0.6)
