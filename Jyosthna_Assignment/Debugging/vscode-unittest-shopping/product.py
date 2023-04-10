class Product:
    def __init__(self, name, price):
        if type(name)!=str or type(price)!=float:
            raise TypeError 
        elif price<0:
            raise ValueError
        else:
            self.name = name
            self.price = price
