
class Product:
    def __init__(self, name, id_product, price, ):
        self.__name = name
        self.__id_product = id_product
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def id_product(self):
        return self.__id_product

    @property
    def price(self):
        return self.price
