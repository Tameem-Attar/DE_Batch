class Product:
    def __init__(self, name, price):
        if type(name)!=str or type(price)!= float:
            raise TypeError
        elif price<0:
            raise ValueError
        elif type(name)==str and type(price)==float:
            self.name=name
            self.price = price       