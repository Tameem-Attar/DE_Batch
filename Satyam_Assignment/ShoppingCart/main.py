from product import Product
from shoppingcart import ShoppingCart

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